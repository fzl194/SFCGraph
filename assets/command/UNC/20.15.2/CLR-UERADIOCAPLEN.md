---
id: UNC@20.15.2@MMLCommand@CLR UERADIOCAPLEN
type: MMLCommand
name: CLR UERADIOCAPLEN（清除UE Radio Capability信元长度统计信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: UERADIOCAPLEN
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- UE无线能力控制策略
status: active
---

# CLR UERADIOCAPLEN（清除UE Radio Capability信元长度统计信息）

## 功能

**适用NF：AMF**

该命令用于清除AMF存储的UE Radio Capability信元长度统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/UERADIOCAPLEN]] · UE Radio Capability信元长度（UERADIOCAPLEN）

## 使用实例

清除UE Radio Capability信元长度统计信息，执行如下命令：

```
CLR UERADIOCAPLEN:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除UE-Radio-Capability信元长度统计信息（CLR-UERADIOCAPLEN）_71436527.md`
