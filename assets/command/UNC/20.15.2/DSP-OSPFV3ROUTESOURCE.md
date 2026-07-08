---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3ROUTESOURCE
type: MMLCommand
name: DSP OSPFV3ROUTESOURCE（查询OSPFv3路由源信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3ROUTESOURCE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- OSPF调测
status: active
---

# DSP OSPFV3ROUTESOURCE（查询OSPFv3路由源信息）

## 功能

该命令用于查询OSPFv3的路由源信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| DESTIPV6ADDR | 目的IPv6地址 | 可选必选说明：必选参数<br>参数含义：目的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | 前缀长度 | 可选必选说明：必选参数<br>参数含义：前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3ROUTESOURCE]] · OSPFv3路由源信息（OSPFV3ROUTESOURCE）

## 使用实例

查询OSPFv3进程1中目的IPv6地址为2001:db8::2、前缀长度为64的路由源信息：

```
DSP OSPFV3ROUTESOURCE:PROCESSID=1,DESTIPV6ADDR="2001:db8::2",IPV6MASKLEN=64;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                      进程号  =  1
              本地路由器标识  =  10.1.1.1
                目的IPv6地址  =  2001:db8::2
                    前缀长度  =  64
                路由标志信息  =  0xe1008063
                      路由锁  =  4
                  路由源序号  =  1
       LSA报文中的链路状态ID  =  10.1.1.1
                  路由源类型  =  直连路由
              宣告路由器标识  =  10.1.1.1
                    区域标识  =  0.0.0.0
                  路径Cost值  =  1
            实际生效的开销值  =  1
                  开销值类型  =  1
                        标签  =  1
                路由源标记值  =  0xe0181b48
                下一跳IP地址  =  0.0.0.0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFV3ROUTESOURCE.md`
