---
id: UDG@20.15.2@MMLCommand@LST BGPPEERGROUPBFD
type: MMLCommand
name: LST BGPPEERGROUPBFD（查询BGP对等体组BFD检测）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BGPPEERGROUPBFD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体组BFD检测
status: active
---

# LST BGPPEERGROUPBFD（查询BGP对等体组BFD检测）

## 功能

该命令用于查看对等体组的BFD参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| GROUPNAME | 组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |
| AFTYPE | 组地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- public：公网地址族。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>- noaf：不指定地址族。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPPEERGROUPBFD]] · BGP对等体组BFD检测（BGPPEERGROUPBFD）

## 使用实例

查看对等体组的BFD参数：

```
LST BGPPEERGROUPBFD:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
          VPN实例名称  =  vpna
                 组名  =  asdf
         组地址族类型  =  IPv4uni
         检测时间倍数  =  3
          BFD是否使能  =  TRUE
最小接收间隔时间（ms） =  200
最小发送间隔时间（ms） =  300
         使能单跳模式  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BGPPEERGROUPBFD.md`
