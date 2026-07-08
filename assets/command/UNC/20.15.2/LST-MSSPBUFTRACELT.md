---
id: UNC@20.15.2@MMLCommand@LST MSSPBUFTRACELT
type: MMLCommand
name: LST MSSPBUFTRACELT（查询PBUF轨迹开关状态和持续时间）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MSSPBUFTRACELT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 轨迹开关
status: active
---

# LST MSSPBUFTRACELT（查询PBUF轨迹开关状态和持续时间）

## 功能

该命令用于查询PBUF轨迹开关状态和持续时间。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSPBUFTRACELT]] · PBUF轨迹开关状态和持续时间（MSSPBUFTRACELT）

## 使用实例

查询当前PBUF轨迹开关状态和持续时间:

```
%%LST MSSPBUFTRACELT:;%%
RETCODE = 0  操作成功

结果如下
--------
            PBUF轨迹开关  =  开
轨迹开关持续时间（分钟）  =  1440
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MSSPBUFTRACELT.md`
