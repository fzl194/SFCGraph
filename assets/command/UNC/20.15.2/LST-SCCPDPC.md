---
id: UNC@20.15.2@MMLCommand@LST SCCPDPC
type: MMLCommand
name: LST SCCPDPC（查询SCCP目的信令点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPDPC
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
- SCCP目的信令点
status: active
---

# LST SCCPDPC（查询SCCP目的信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP目的信令点表中指定的记录。

## 注意事项

- 没有输入参数，表示查询所有记录。
- 输入目的信令点索引，查询对应目的信令点索引的记录。
- 输入目的信令点名，查询对应目的信令点名的记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DPX | 目的信令点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点索引。<br>前提条件：此目的信令点索引记录必须在SCCP目的信令点表中存在，通过命令<br>[**LST SCCPDPC**](查询SCCP目的信令点(LST SCCPDPC)_72225999.md)<br>查询。<br>取值范围：0~1279<br>默认值：无 |
| DPN | 目的信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点名。<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPC]] · SCCP目的信令点（SCCPDPC）

## 使用实例

1. 查询SCCP目的信令点表中所有记录：
  LST SCCPDPC:;
  ```
  %%LST SCCPDPC:;%%
  RETCODE = 0  操作成功。

  SCCP目的信令点表
  ----------------
   目的信令点索引  本局信令点索引  网络指示语  目的信令点编码  协议类型  负荷分担类型  负荷分担目的信令点索引  备用目的信令点索引  目的信令点名

   3               1               国内备用网  0x3373          ITUT_SS7  不使用        NULL                    NULL                beijing    
   4               2               国内网      0x103701        ITUT_SS7  不使用        NULL                    NULL                R6Rnc     
   1               1               国内备用网  0x3371          ITUT_SS7  不使用        NULL                    NULL                R8Rnc    
  (结果个数 = 3)

  ---    END
  ```
2. 查询目的信令点索引为3，目的信令点名为beijing的记录：
  LST SCCPDPC: DPX=3, DPN="beijing";
  ```
  %%LST SCCPDPC: DPX=3, DPN="beijing";%%
  RETCODE = 0  操作成功。

  SCCP目的信令点表
  ----------------
          目的信令点索引  =  3
          本局信令点索引  =  1
              网络指示语  =  国内备用网
          目的信令点编码  =  0x3373
                协议类型  =  ITUT_SS7
            负荷分担类型  =  不使用
  负荷分担目的信令点索引  =  NULL
      备用目的信令点索引  =  NULL
            目的信令点名  =  beijing
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCCPDPC.md`
