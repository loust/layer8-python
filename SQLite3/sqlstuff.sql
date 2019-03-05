SELECT master.id FROM master        -- select id from master table
WHERE id is ? AND sid is ?          -- where id is given and server id is given
UNION SELECT slave.id FROM slave    -- union and select slave table, grab id coulmn from slave table
WHERE id is ? AND sid is ?;         -- id and server id is as given


SELECT DISTINCT                               -- Distinct implies unique
CASE                                          -- If
    WHEN master.id IS ? AND master.sid IS ?   -- if id of master is given and server id of master is given
        THEN 'Master'                         -- Label the column as 'Master'
    WHEN slave.id IS ? AND slave.sid IS ?     -- if id of slave is given and the server id of slave is given
        THEN 'Slave'                          -- label column as 'Slave'
END Status                                    -- Give this a name, called "Status"
FROM master, slave                            -- We are getting it from both of these tables
WHERE Status IS NOT NULL;                     -- If the output "Status" is not null, show output.


SELECT DISTINCT master.id     -- A unique/deduped id from master table
FROM master, slave            -- Get values from both tables. Master and slave
WHERE master.sid is ?         -- server ID of master is given
AND slave.sid is ?            -- Logical AND it with the server ID of slave's ID of given server ID
AND master.connect is ?       -- Logical AND it with the connection of slave ID from the master table is as given
AND slave.id is ?;            -- Logical AND it with the slave's ID as is given from the slave table
