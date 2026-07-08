---
id: UNC@20.15.2@MMLCommand@LST 5GCQOSCORRT
type: MMLCommand
name: LST 5GCQOSCORRT（查询5GC QoS纠错配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: 5GCQOSCORRT
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 全局5GC QoS纠错
status: active
---

# LST 5GCQOSCORRT（查询5GC QoS纠错配置）

## 功能

**适用NF：SMF**

该命令用来查询当SMF收到UE、UDM或PCF消息中携带的QoS字段不合法时，使用该配置作为纠错后的5G QoS参数值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [5GC QoS纠错配置（5GCQOSCORRT）](configobject/UNC/20.15.2/5GCQOSCORRT.md)

## 使用实例

查询5GC QoS纠错配置：

```
%%LST 5GCQOSCORRT:;%%
RETCODE = 0  操作成功

操作结果如下
------------
下行Session AMBR(千比特/秒)  =  20000
上行Session AMBR(千比特/秒)  =  20000
                      5QI值  =  5
                      ARP值  =  3
    上行保证带宽(千比特/秒)  =  4000
    下行保证带宽(千比特/秒)  =  4000
    下行最大带宽(千比特/秒)  =  5000
    上行最大带宽(千比特/秒)  =  5000
                  5QI优先级  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5GC-QoS纠错配置（LST-5GCQOSCORRT）_09651697.md`
