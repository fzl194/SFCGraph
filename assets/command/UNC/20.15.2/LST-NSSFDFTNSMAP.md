---
id: UNC@20.15.2@MMLCommand@LST NSSFDFTNSMAP
type: MMLCommand
name: LST NSSFDFTNSMAP（查询漫游切片默认映射配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFDFTNSMAP
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF漫游配置管理
status: active
---

# LST NSSFDFTNSMAP（查询漫游切片默认映射配置）

## 功能

**适用NF：NSSF**

该命令用于查询漫游切片默认映射配置。

若要查询全部漫游切片默认映射的配置信息，请不要输入任何参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLMODE | 控制模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于用户归属PLMN还是拜访地PLMN进行切片映射。<br>数据来源：全网规划<br>取值范围：<br>- “VPLMN（拜访地PLMN）”：拜访地PLMN<br>- “HPLMN（归属地PLMN）”：归属地PLMN<br>默认值：无<br>配置原则：无 |
| VMCC | 拜访地移动国家码 | 可选必选说明：该参数在"CTRLMODE"配置为"VPLMN"时为条件可选参数。<br>参数含义：该参数用于描述拜访地移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| VMNC | 拜访地移动网号 | 可选必选说明：该参数在"CTRLMODE"配置为"VPLMN"时为条件可选参数。<br>参数含义：该参数用于描述拜访地移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| HMCC | 归属地移动国家码 | 可选必选说明：该参数在"CTRLMODE"配置为"HPLMN"时为条件可选参数。<br>参数含义：该参数用于指定归属地移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| HMNC | 归属地移动网号 | 可选必选说明：该参数在"CTRLMODE"配置为"HPLMN"时为条件可选参数。<br>参数含义：该参数用于指定归属地移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFDFTNSMAP]] · 漫游切片默认映射配置（NSSFDFTNSMAP）

## 使用实例

- 查询“拜访地移动国家码”为“123”、“拜访地移动网号”为“45”的SrvPLMN配置的默认切片映射配置，执行如下命令：
  ```
  %%LST NSSFDFTNSMAP: CTRLMODE=VPLMN, VMCC="123", VMNC="45";%%
  RETCODE = 0  操作成功
 
  结果如下
  --------
                控制模式  =  拜访地PLMN
        拜访地移动国家码  =  123
          拜访地移动网号  =  45
        归属地移动国家码  =  NULL
          归属地移动网号  =  NULL
  拜访地默认切片服务类型  =  8
  拜访地默认切片细分标识  =  ABC123
  (结果个数 = 1)
 
  ---    END
  ```
- 查询所有的漫游切片默认映射配置，执行如下命令：
  ```
  %%LST NSSFDFTNSMAP:;%%
  RETCODE = 0  操作成功
 
  结果如下
  --------
  控制模式      拜访地移动国家码     拜访地移动网号     归属地移动国家码     归属地移动网号     拜访地默认切片服务类型     拜访地默认切片细分标识
  拜访地PLMN    123                  45                 NULL                 NULL               8                          ABC123
  拜访地PLMN    245                  23                 NULL                 NULL               8                          ABC123
  (结果个数 = 2)
 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSFDFTNSMAP.md`
