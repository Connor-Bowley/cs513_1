// Import the following packages to use JDBC.
import  java.sql.*;
import  java.io.*;
import  oracle.jdbc.*;
import  oracle.jdbc.pool.OracleDataSource;

class  FullDevInfo{
    public static void  main( String args[ ] ) throws SQLException {
		if(args.length == 0)
		{
			return;
		}
		String user     = "cbowley";
		String password = "secrets";
		String database = "oracle1.aero.und.edu:1521/cs513.aero.und.edu";

		// Open an OracleDataSource and get a connection.
		OracleDataSource ods = new OracleDataSource( );
		ods.setURL     ( "jdbc:oracle:thin:@" + database );
		ods.setUser    ( user );
		ods.setPassword( password );
		Connection conn = ods.getConnection( );
		
		try
		{
			Statement state_info = conn.createStatement(), state_games = conn.createStatement();
			String query_info  = "SELECT id, name FROM developers WHERE id = " + args[0];
			String query_games = "SELECT g.asin, g.title, g.price FROM games g, developers d WHERE d.id = " + args[0] + " AND d.id IN (SELECT * FROM table(g.developers))";

			ResultSet rset_info  = state_info.executeQuery(query_info);
			ResultSet rset_games = state_games.executeQuery(query_games);

			StringBuilder builder = new StringBuilder();
			builder.append("{");
			boolean firstTime = true;
			if(rset_info.next())
			{
				builder.append("\"Id\":\"");
				builder.append(rset_info.getString(1));
				builder.append("\",\"Name\":\"");
				builder.append(rset_info.getString(2));
				builder.append("\",");
			}
			builder.append("\"Games\":[");
			while(rset_games.next())
			{
				if(firstTime)
					firstTime = false;
				else
					builder.append(",");

				builder.append("{\"Asin\":\"");
				builder.append(rset_games.getString(1));
				builder.append("\",\"Title\":\"");
				builder.append(rset_games.getString(2));
				builder.append("\",\"Price\":\"");
				builder.append(String.format("%.2f",Float.parseFloat(rset_games.getString(3))));
				builder.append("\"}");
			}
			builder.append("]}");

			System.out.println(builder.toString());

			rset_info.close();
			rset_games.close();
			state_info.close();
			state_games.close();
		}
		catch(SQLException e)
		{
			e.printStackTrace();
		}
		conn.close();
	}
}
