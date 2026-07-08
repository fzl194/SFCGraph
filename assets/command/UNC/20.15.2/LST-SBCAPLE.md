---
id: UNC@20.15.2@MMLCommand@LST SBCAPLE
type: MMLCommand
name: LST SBCAPLE（查询SBCAP本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBCAPLE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBCAP本地实体
status: active
---

# LST SBCAPLE（查询SBCAP本地实体）

## 功能

**适用网元：MME**

该命令用于查看SBc链路本地实体配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 本端实体号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的SBc链路本地实体号。<br>取值范围：0～127<br>默认值：无<br>说明：如果不输入，则表示查询系统内所有SBc链路本地实体配置数据。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBCAPLE]] · SBCAP本地实体（SBCAPLE）

## 使用实例

1. 不输入SBc链路本地实体号，查询所有SBc链路本地实体配置数据：
  LST SBCAPLE:;
  ```
  %%LST SBCAPLE:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
  本端实体号    IP地址类型    本地IP地址1    本地IP地址2        本地端口号    SCTP协议参数索引    交叉路径是否可用    本端实体名称    vpn名称

  0             IPv4          10.0.0.1       255.255.255.255    29168         0                   否                  noname          NULL   
  1             IPv4          10.0.0.1       255.255.255.255    29169         0                   否                  noname          NULL 
  (结果个数 = 2)
  ---    END
  ```
2. 输入SBCAP链路本地实体号，查询指定的SBCAP链路本地实体配置数据：
  LST SBCAPLE: LLEINDEX=1;
  ```
  %%LST SBCAPLE: LLEINDEX=1;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
        本端实体号  =  1
        IP地址类型  =  IPv4
       本地IP地址1  =  10.0.0.1
       本地IP地址2  =  255.255.255.255
        本地端口号  =  29169
  SCTP协议参数索引  =  0
  交叉路径是否可用  =  否
      本端实体名称  =  noname
           vpn名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SBCAPLE.md`
