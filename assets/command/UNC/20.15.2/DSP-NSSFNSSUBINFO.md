---
id: UNC@20.15.2@MMLCommand@DSP NSSFNSSUBINFO
type: MMLCommand
name: DSP NSSFNSSUBINFO（显示订阅任务信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFNSSUBINFO
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFNSSUBINFO（显示订阅任务信息）

## 功能

**适用NF：NSSF**

该命令用于查询所有AMF的订阅任务信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFNSSUBINFO]] · 订阅任务信息（NSSFNSSUBINFO）

## 使用实例

当运营商想要查询所有AMF在NSSF上的订阅信息时，执行此命令

```
DSP NSSFNSSUBINFO:;
%%DSP NSSFNSSUBINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
订阅标识                              通知URI                                                                               AMF集合标识    通知事件类型                 订阅有效期    订阅的TAI数目

0004c7d76079f5a24517a4e03d90e484975c  http://10.70.183.1:5160/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  460-03-01-001  SNSSAI_STATUS_CHANGE_REPORT  1599895763    1
000154b35ab273514635a90f527d3a4a01d1  http://10.70.183.2:5260/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  460-03-01-001  SNSSAI_STATUS_CHANGE_REPORT  1599895764    1
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示订阅任务信息（DSP-NSSFNSSUBINFO）_96241983.md`
