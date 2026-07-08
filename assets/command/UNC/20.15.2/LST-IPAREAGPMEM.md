---
id: UNC@20.15.2@MMLCommand@LST IPAREAGPMEM
type: MMLCommand
name: LST IPAREAGPMEM（查询IP区域群成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPAREAGPMEM
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于位置分配IP地址管理
- IP区域群成员管理
status: active
---

# LST IPAREAGPMEM（查询IP区域群成员）

## 功能

**适用网元：SGSN、MME**

该命令用于查询区域群成员记录。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：待查询的区域群标识。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |
| IDTYPE | 标识类型 | 可选必选说明：可选参数<br>参数含义：待查询的区域标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “LAC(位置区域码)”<br>- “TAC(跟踪区域码)”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件可选参数<br>参数含义：待查询的位置区域码。<br>前提条件：该参数在“IDTYPE(标识类型)”设置为“LAC(位置区)”时生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件可选参数<br>参数含义：待查询的跟踪区域码。<br>前提条件：该参数在“IDTYPE(标识类型)”设置为“TAC(跟踪区)”时生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPAREAGPMEM]] · IP区域群成员（IPAREAGPMEM）

## 使用实例

1. 不输入查询条件，查询表中全部区域群成员的信息：
  LST IPAREAGPMEM:;
  ```
  %%LST IPAREAGPMEM:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   区域群标识  标识类型     位置区域码   跟踪区域码                                                                                                    
   1           位置区域码   0x1234       NULL                                                                                                                   
   2           跟踪区域码   NULL         0x3456      
  (结果个数 = 2)

  ---    END
  ```
2. 查询一条区域群标识为1的区域群成员记录：
  LST IPAREAGPMEM: AREAID=1;
  ```
  %%LST IPAREAGPMEM: AREAID=1;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------       
       区域群标识  =  1
         标识类型  =  位置区域码
       位置区域码  =  0x1234
       跟踪区域码  =  NULL

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPAREAGPMEM.md`
