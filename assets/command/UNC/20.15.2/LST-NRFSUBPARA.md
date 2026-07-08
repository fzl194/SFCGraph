---
id: UNC@20.15.2@MMLCommand@LST NRFSUBPARA
type: MMLCommand
name: LST NRFSUBPARA（查询NRF订阅参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSUBPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF订阅参数
status: active
---

# LST NRFSUBPARA（查询NRF订阅参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF订阅参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFSUBPARA]] · NRF订阅参数（NRFSUBPARA）

## 使用实例

当运营商希望查询NRF订阅参数信息时，执行此命令。

```
LST NRFSUBPARA:;
%%LST NRFSUBPARA:;%%
RETCODE = 0  操作成功
结果如下
--------
   订阅记录老化宽限时长(秒)   =  60
       订阅记录有效宽限开关   =  开启
   订阅记录有效宽限时长(秒)   =  30
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSUBPARA.md`
