---
id: UNC@20.15.2@MMLCommand@DSP VNFINNERSTAT
type: MMLCommand
name: DSP VNFINNERSTAT（显示网元内部状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VNFINNERSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- VNF状态管理
status: active
---

# DSP VNFINNERSTAT（显示网元内部状态）

## 功能

该命令用于显示网元的内部状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFINNERSTAT]] · 网元内部状态（VNFINNERSTAT）

## 使用实例

当运营商需要对网元进行操作（如升级、补丁等）时，可以使用该命令查询网元内部状态，提前识别风险。

```
%%DSP VNFINNERSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
分类      状态  备注  

POD状态   正常  NULL  
服务状态  正常  NULL  
规格状态  正常  NULL  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示网元内部状态（DSP-VNFINNERSTAT）_36685937.md`
