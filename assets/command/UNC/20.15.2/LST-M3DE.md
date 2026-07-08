---
id: UNC@20.15.2@MMLCommand@LST M3DE
type: MMLCommand
name: LST M3DE（查询M3UA目的实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M3DE
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
- M3UA目的实体
status: active
---

# LST M3DE（查询M3UA目的实体）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于查询M3UA目的实体的配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEX | 目的实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定唯一标示目的实体的索引。<br>取值范围：0~1279<br>默认值：无<br>配置原则：无 |
| DEN | 目的实体名 | 选必选说明：可选参数<br>参数含义：该参数用于指定目的实体的名称。<br>取值范围：长度不超过32的字符串<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3DE]] · M3UA目的实体（M3DE）

## 使用实例

1. 不输入查询参数，查询已经配置的所有目的实体数据：
  ```
  LST M3DE:;
  ```
  ```
  %%LST M3DE:;%%
  RETCODE = 0  操作成功。

  M3UA目的实体表
  --------------
   目的实体索引  本地实体索引  目的实体编码  链路集选择掩码  信令转接点功能  目的实体类型    相邻标记  网络模式    路由上下文  M3UA协议版本  目的实体名

   2             3             0x111         B0000           否              IP服务进程      是        独占信令点  2           支持RFC3332   noname    
   5             2             0x112         B0000           否              IP服务进程      是        独占信令点  1           支持RFC3332   aaa       
  (结果个数 = 2)

  ---    END
  ```
2. 输入目的实体索引，查询指定的M3UA目的实体数据：
  ```
  LST M3DE: DEX=2;
  ```
  ```
  %%LST M3DE: DEX=2;%%
  RETCODE = 0  操作成功。

  M3UA目的实体表
  --------------
    目的实体索引  =  2
    本地实体索引  =  3
    目的实体编码  =  0x111
  链路集选择掩码  =  B0000
  信令转接点功能  =  否
    目的实体类型  =  IP服务进程
        相邻标记  =  是
        网络模式  =  独占信令点
      路由上下文  =  2
    M3UA协议版本  =  支持RFC3332
      目的实体名  =  noname
  (结果个数 = 1)

  ---    END
  ```
3. 输入目的实体名，查询指定的M3UA目的实体数据：
  ```
  LST M3DE: DEN="aaa";
  ```
  ```
  %%LST M3DE: DEN="aaa";%%
  RETCODE = 0  操作成功。

  M3UA目的实体表
  --------------
    目的实体索引  =  5
    本地实体索引  =  2
    目的实体编码  =  0x112
  链路集选择掩码  =  B0000
  信令转接点功能  =  否
    目的实体类型  =  IP服务进程
        相邻标记  =  是
        网络模式  =  独占信令点
      路由上下文  =  1
    M3UA协议版本  =  支持RFC3332
      目的实体名  =  aaa
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-M3DE.md`
