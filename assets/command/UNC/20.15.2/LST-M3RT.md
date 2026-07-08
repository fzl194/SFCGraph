---
id: UNC@20.15.2@MMLCommand@LST M3RT
type: MMLCommand
name: LST M3RT（查询M3UA信令路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M3RT
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
- M3UA管理
- M3UA路由
status: active
---

# LST M3RT（查询M3UA信令路由）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于查询M3UA信令路由配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RTX | 路由索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定准备显示的路由的索引。<br>取值范围：0~1279<br>默认值：无 |
| DEX | 目的实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该M3UA路由的目的实体。<br>取值范围：0~1279<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定到达该的目的实体的M3UA链路集。<br>取值范围：0~1279<br>默认值：无 |
| RTN | 信令路由名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识M3UA路由。<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M3RT]] · M3UA信令路由（M3RT）

## 使用实例

1. 不输入查询参数，查询已经配置的所有信令路由数据：
  LST M3RT:;
  ```
  %%LST M3RT:;%%
  RETCODE = 0  操作成功。

  M3UA路由表
  ----------
   路由索引  目的实体索引  链路集索引  优先级  信令路由名

   0         0             0           0     R6_MNT_M3UA_ST_01
   1         1             1           0     R6_M3RT1
  (结果个数 = 2)

  ---    END
  ```
2. 输入路由索引，查询指定的M3UA信令路由数据：
  LST M3RT: RTX=0;
  ```
  %%LST M3RT: RTX=0;%%
  RETCODE = 0  操作成功。

  M3UA路由表
  ----------
      路由索引  =  0
  目的实体索引  =  0
    链路集索引  =  0
        优先级  =  0
    信令路由名  =  R6_MNT_M3UA_ST_01
  (结果个数 = 1)

  ---    END
  ```
3. 输入目的实体索引，查询指定的M3UA信令路由数据：
  LST M3RT: DEX=1;
  ```
  %%LST M3RT: DEX=1;%%
  RETCODE = 0  操作成功。

  M3UA路由表
  ----------
      路由索引  =  1
  目的实体索引  =  1
    链路集索引  =  1
        优先级  =  0
    信令路由名  =  R6_M3RT1
  (结果个数 = 1)

  ---    END
  ```
4. 输入链路集索引，查询指定的M3UA信令路由数据：
  LST M3RT: LSX=1;
  ```
  %%LST M3RT: LSX=1;%%
  RETCODE = 0  操作成功。

  M3UA路由表
  ----------
      路由索引  =  1
  目的实体索引  =  1
    链路集索引  =  1
        优先级  =  0
    信令路由名  =  R6_M3RT1
  (结果个数 = 1)

  ---    END
  ```
5. 输入信令路由名，查询指定的M3UA信令路由数据：
  LST M3RT: RTN="R6_M3RT1";
  ```
  %%LST M3RT: RTN="R6_M3RT1";%%
  RETCODE = 0  操作成功。

  M3UA路由表
  ----------
      路由索引  =  1
  目的实体索引  =  1
    链路集索引  =  1
        优先级  =  0
    信令路由名  =  R6_M3RT1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-M3RT.md`
