---
id: UNC@20.15.2@MMLCommand@LST S1APLE
type: MMLCommand
name: LST S1APLE（查询S1AP本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1APLE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP本地实体
status: active
---

# LST S1APLE（查询S1AP本地实体）

## 功能

**适用网元：MME**

该命令用于查看S1AP链路本地实体配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 链路本地实体号 | 可选必选说明：可选参数<br>参数含义：待查询的S1AP链路本地实体号。<br>取值范围：0～63<br>默认值：无<br>说明：如果不输入，则表示查询系统内所有S1AP链路配置数据。 |

## 操作的配置对象

- [S1AP本地实体（S1APLE）](configobject/UNC/20.15.2/S1APLE.md)

## 使用实例

1. 不输入S1AP链路本地实体号，查询已经配置的所有S1AP链路数据：
  LST S1APLE:;
  ```
  %%LST S1APLE:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   链路本地实体号  IP地址类型  本地IP地址1     本地IP地址2      本地端口号  交叉路径是否可用  SCTP协议参数索引  链路本地实体名  VPN名称 

   0               Ipv4        192.168.15.10   255.255.255.255  36412       否                0                 To-eNodeB0      _abc_    
   1               Ipv4        192.168.15.10   255.255.255.255  36413       否                0                 To-eNodeB1      _abc_
  (结果个数 = 2)

  ---    END
  ```
2. 输入S1AP链路本地实体号，查询指定的S1AP链路数据：
  LST S1APLE: LLEINDEX=0;
  ```
  %%LST S1APLE: LLEINDEX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
    链路本地实体号  =  0
        IP地址类型  =  Ipv4
       本地IP地址1  =  192.168.15.10
       本地IP地址2  =  255.255.255.255
        本地端口号  =  36412
  交叉路径是否可用  =  否
  SCTP协议参数索引  =  0
    链路本地实体名  =  To-eNodeB0
           VPN名称  =  _abc_
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1AP本地实体(LST-S1APLE)_72345855.md`
