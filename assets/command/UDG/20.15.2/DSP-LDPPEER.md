---
id: UDG@20.15.2@MMLCommand@DSP LDPPEER
type: MMLCommand
name: DSP LDPPEER（显示LDP邻居）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP邻居管理
status: active
---

# DSP LDPPEER（显示LDP邻居）

## 功能

该命令用于显示LDP邻居。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PEERLSRID | 邻居LDP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LDP标识符，格式为<LSR ID>：<标签空间>。标签空间取值： “0”表示全局标签空间。 “1”表示接口标签空间。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [LDP邻居（LDPPEER）](configobject/UDG/20.15.2/LDPPEER.md)

## 使用实例

显示LDP邻居：

```
DSP LDPPEER:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                  VPN实例名称  =  _public_
                   邻居LDP ID  =  192.168.1.2:0
              邻居最大PDU长度  =  4096
             邻居环路探测状态  =  FALSE
                   邻居FT标志  =  FALSE
                 邻居传输地址  =  192.168.1.2
           邻居路径向量限制值  =  0
 邻居keepalive定时器时间（s）  =  45
  邻居recovery定时器的值（s）  =  NULL
   邻居reconnect定时器值（s）  =  NULL
             邻居标签发布方式  =  DU
             邻居动态协商能力  =  DISABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LDP邻居（DSP-LDPPEER）_00441101.md`
