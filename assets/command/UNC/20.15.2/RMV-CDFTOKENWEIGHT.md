---
id: UNC@20.15.2@MMLCommand@RMV CDFTOKENWEIGHT
type: MMLCommand
name: RMV CDFTOKENWEIGHT（删除cdf token权重）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDFTOKENWEIGHT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- CDF token权重
status: active
---

# RMV CDFTOKENWEIGHT（删除cdf token权重）

## 功能

![](删除cdf token权重（RMV CDFTOKENWEIGHT）_39919397.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且删除cdf token权重配置时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于删除cdf token权重配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于描述pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDFTOKENWEIGHT]] · cdf token权重（CDFTOKENWEIGHT）

## 使用实例

当删除pod名称为cgfb-pod-0上的cdf token权重配置：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-06-11 15:20:20+8:00
O&M    #3546
%%RMV CDFTOKENWEIGHT: PODNAME="cgfb-pod-0", CONFIRM=Y;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除cdf-token权重（RMV-CDFTOKENWEIGHT）_39919397.md`
