---
id: UNC@20.15.2@MMLCommand@LST PLCYCKTIMERINR
type: MMLCommand
name: LST PLCYCKTIMERINR（查询策略类型和核查间隔）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLCYCKTIMERINR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# LST PLCYCKTIMERINR（查询策略类型和核查间隔）

## 功能

该命令用于查询策略类型和核查间隔。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYCKTIMERINR]] · 策略类型和核查间隔（PLCYCKTIMERINR）

## 使用实例

查询策略类型和核查间隔，内部策略用inner strategy，外部策略用outer strategy，核查间隔单位为分钟。

```
%%LST PLCYCKTIMERINR:;%%
RETCODE = 0  操作成功

结果如下
------------------------             
策略类型   策略核查时间间隔 (分钟) 
内部策略           1
外部通信策略    10
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PLCYCKTIMERINR.md`
