---
id: UDG@20.15.2@MMLCommand@LST SBILNKCTRLSW
type: MMLCommand
name: LST SBILNKCTRLSW（查询服务化接口链路自动控制功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SBILNKCTRLSW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路控制管理
status: active
---

# LST SBILNKCTRLSW（查询服务化接口链路自动控制功能开关）

## 功能

该命令用于查询服务化接口链路自动控制功能是否开启。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [服务化接口链路自动控制功能开关（SBILNKCTRLSW）](configobject/UDG/20.15.2/SBILNKCTRLSW.md)

## 使用实例

运营商想要查询服务化接口链路自动控制功能是否开启。

```
LST SBILNKCTRLSW:;

%%LST SBILNKCTRLSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
       链路控制开关  =  OFF
             起始位  =  9
             结束位  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务化接口链路自动控制功能开关（LST-SBILNKCTRLSW）_83813636.md`
