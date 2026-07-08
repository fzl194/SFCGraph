---
id: UDG@20.15.2@MMLCommand@LST ARPINTERFACE
type: MMLCommand
name: LST ARPINTERFACE（查询接口下ARP配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPINTERFACE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- 接口下ARP配置
status: active
---

# LST ARPINTERFACE（查询接口下ARP配置信息）

## 功能

在监控ARP表项或APP出现故障时，可以使用此命令查看ARP表项的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：以太网接口名称由接口类型和接口编号组成。 |

## 操作的配置对象

- [接口下ARP配置信息（ARPINTERFACE）](configobject/UDG/20.15.2/ARPINTERFACE.md)

## 使用实例

查询Ethernet64/0/5的接口配置：

```
LST ARPINTERFACE:IFNAME="Ethernet64/0/5";
```

```

RETCODE = 0  操作成功。

结果如下
--------
  表项老化时间（s）  =  1200
  老化探测间隔（s）  =  5
       老化探测次数  =  3
    ARP关闭动态学习  =  FALSE
    ARP严格学习类型  =  信任
         路由式代理  =  FALSE
假表项老化时间（s）  =  5
           单播探测  =  FALSE
        目的MAC检查  =  FALSE
          源MAC检查  =  FALSE
           接口名称  =  Ethernet64/0/5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口下ARP配置信息（LST-ARPINTERFACE）_49961278.md`
