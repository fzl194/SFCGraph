---
id: UNC@20.15.2@MMLCommand@LST M3LE
type: MMLCommand
name: LST M3LE（查询M3UA本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M3LE
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA本地实体
status: active
---

# LST M3LE（查询M3UA本地实体）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于查询M3UA本地实体的配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备查询的本地实体的索引。<br>取值范围：0~63<br>默认值：无<br>配置原则：无 |
| LEN | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定标识本地实体。<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LE]] · M3UA本地实体（M3LE）

## 使用实例

1. 不输入查询参数，查询已经配置的所有本地实体数据：
  ```
  LST M3LE:;
  ```
  ```
  %%LST M3LE:;%%
  RETCODE = 0  操作成功。

  M3UA本地实体表
  --------------
   本地实体索引  网络指示语  本地实体编码  本地实体类型  路由上下文 网络外貌 本地实体名

   0             国内网      0xAAA         IP服务进程     NULL        NULL   Test_M3le1
   1             国内网      0x12          信令网关进程   NULL        NULL   Test_M3le2
  (结果个数 = 2)

  ---    END
  ```
2. 输入本地实体索引，查询指定的M3UA本地实体数据：
  ```
  LST M3LE: LEX=1;
  ```
  ```
  %%LST M3LE: LEX=1;%%
  RETCODE = 0  操作成功。

  M3UA本地实体表
  --------------
  本地实体索引  =  1
    网络指示语  =  国内网
  本地实体编码  =  0x12
  本地实体类型  =  信令网关进程
    路由上下文  =  NULL
      网络外貌  =  NULL
    本地实体名  =  Test_M3le2
  (结果个数 = 1)

  ---    END
  ```
3. 输入本地实体名，查询指定的M3UA本地实体数据：
  ```
  LST M3LE: LEN="Test_M3le1";
  ```
  ```
  %%LST M3LE: LEN="Test_M3le1";%%
  RETCODE = 0  操作成功。

  M3UA本地实体表
  --------------
  本地实体索引  =  0
    网络指示语  =  国内网
  本地实体编码  =  0xAAA
  本地实体类型  =  IP服务进程
    路由上下文  =  NULL
      网络外貌  =  NULL
    本地实体名  =  Test_M3le1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M3UA本地实体(LST-M3LE)_72225993.md`
