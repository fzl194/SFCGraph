---
id: UDG@20.15.2@MMLCommand@LST ARPSYS
type: MMLCommand
name: LST ARPSYS（查询ARP系统信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPSYS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# LST ARPSYS（查询ARP系统信息）

## 功能

该命令用于查看ARP系统老化时间、全局ARP严格学习使能、ARP日志告警上报时间间隔和免费ARP发送类型。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [ARP系统信息（ARPSYS）](configobject/UDG/20.15.2/ARPSYS.md)

## 使用实例

查询ARP系统配置信息：

```
LST ARPSYS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
           表项老化时间（s）  =  1200
         全局ARP严格学习使能  =  FALSE
ARP日志告警上报时间间隔（s）  =  80
             免费ARP发送类型  =  请求
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ARP系统信息（LST-ARPSYS）_00600693.md`
