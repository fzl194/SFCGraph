---
id: UNC@20.15.2@MMLCommand@LST SCCPDPCSHR
type: MMLCommand
name: LST SCCPDPCSHR（查询DPC多点负荷分担记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPDPCSHR
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP目的信令点多点负荷分担
status: active
---

# LST SCCPDPCSHR（查询DPC多点负荷分担记录）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP目的信令点多点负荷分担表中指定的记录。

## 注意事项

- 没有输入参数，表示查询所有记录。
- 输入主目的信令点索引，查询对应记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAINDPX | 主DPC索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主SCCP目的信令点索引。<br>取值范围：0～1279<br>默认值：无<br>说明：此目的信令点索引记录必须在SCCP目的信令点多点负荷分担表中存在。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPCSHR]] · DPC多点负荷分担记录（SCCPDPCSHR）

## 使用实例

1. 查询SCCP目的信令点多点负荷分担表中所有记录：
  LST SCCPDPCSHR:;
  ```
  %%LST SCCPDPCSHR:;%%
  RETCODE = 0  操作成功。

  SCCP DPC负荷分担表
  ------------------
  主DPC索引    负荷分担DPC的个数    负荷分担DPC1索引    DPC1优先级    负荷分担DPC2索引    DPC2优先级    负荷分担DPC3索引    DPC3优先级    负荷分担DPC4索引    DPC4优先级    负荷分担DPC5索引    DPC5优先级    负荷分担DPC6索引    DPC6优先级    负荷分担DPC7索引    DPC7优先级    负荷分担DPC8索引    DPC8优先级

  60           2                    61                  1             62                  2             NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL      
  61           2                    62                  1             60                  2             NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL          NULL                NULL      
  (结果个数 = 2)
  ---    END
  ```
2. 查询主目的信令点索引为60的记录：
  LST SCCPDPCSHR: MAINDPX=60;
  ```
  %%LST SCCPDPCSHR: MAINDPX=60;%%
  RETCODE = 0  操作成功。

  SCCP DPC负荷分担表
  ------------------
          主DPC索引  =  60
  负荷分担DPC的个数  =  2
   负荷分担DPC1索引  =  61
         DPC1优先级  =  1
   负荷分担DPC2索引  =  62
         DPC2优先级  =  2
   负荷分担DPC3索引  =  NULL
         DPC3优先级  =  NULL
   负荷分担DPC4索引  =  NULL
         DPC4优先级  =  NULL
   负荷分担DPC5索引  =  NULL
         DPC5优先级  =  NULL
   负荷分担DPC6索引  =  NULL
         DPC6优先级  =  NULL
   负荷分担DPC7索引  =  NULL
         DPC7优先级  =  NULL
   负荷分担DPC8索引  =  NULL
         DPC8优先级  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DPC多点负荷分担记录(LST-SCCPDPCSHR)_26146324.md`
