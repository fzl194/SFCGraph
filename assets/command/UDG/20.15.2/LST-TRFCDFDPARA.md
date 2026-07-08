---
id: UDG@20.15.2@MMLCommand@LST TRFCDFDPARA
type: MMLCommand
name: LST TRFCDFDPARA（查询大流量攻击防护配置参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TRFCDFDPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- 大流量攻击防护参数
status: active
---

# LST TRFCDFDPARA（查询大流量攻击防护配置参数）

## 功能

**适用NF：UPF**

该命令用于查询大流量攻击检测配置参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [大流量攻击防护配置参数（TRFCDFDPARA）](configobject/UDG/20.15.2/TRFCDFDPARA.md)

## 使用实例

查询大流量攻击检测配置参数：

```
LST TRFCDFDPARA:;
```

```

RETCODE = 0  操作成功。

大流量攻击防护配置信息
----------------------
            上行CPU阈值  =  80
       上行报文探测周期  =  65
       上行报文比例阈值  =  10
上行报文防护car控制开关  =  使能
       上行报文速率阈值  =  10
            下行CPU阈值  =  80
       下行报文探测周期  =  8
       下行报文比例阈值  =  10
下行报文防护car控制开关  =  使能
       下行报文速率阈值  =  10
         报文防攻击动作  =  丢包
               日志开关  =  使能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大流量攻击防护配置参数（LST-TRFCDFDPARA）_82837758.md`
