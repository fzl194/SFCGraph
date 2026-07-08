---
id: UDG@20.15.2@MMLCommand@LST SRBFDTEMPLET
type: MMLCommand
name: LST SRBFDTEMPLET（查询BFD模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRBFDTEMPLET
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- 配置BFD模板
status: active
---

# LST SRBFDTEMPLET（查询BFD模板）

## 功能

该命令用于查询配置的BFD模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| DESTVRFNAME | 网关地址VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定网关地址所属VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRBFDTEMPLET]] · BFD模板（SRBFDTEMPLET）

## 使用实例

查询BFD模板：

```
LST SRBFDTEMPLET: AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      网关地址VPN  =  _public_
           地址族  =  IPv4单播
         接口名字  =  Invalid0
       路由下一跳  =  10.0.0.1
         本机地址  =  10.0.0.5
最小接收间隔（ms） =  200
最小传输间隔（ms） =  200
         时间倍数  =  3
         DHCP使能  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BFD模板（LST-SRBFDTEMPLET）_50281218.md`
