---
id: UNC@20.15.2@MMLCommand@LST DDNTIMEOUTCTRL
type: MMLCommand
name: LST DDNTIMEOUTCTRL（查询DDN定时器超时参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNTIMEOUTCTRL
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN消息无响应处理策略
status: active
---

# LST DDNTIMEOUTCTRL（查询DDN定时器超时参数）

## 功能

**适用NF：SGW-C**

该命令用于查看当前设置的DDN消息无响应时的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DDN定时器超时参数（DDNTIMEOUTCTRL）](configobject/UNC/20.15.2/DDNTIMEOUTCTRL.md)

## 使用实例

假设运营商需要查看当前设置的DDN消息无响应时的参数：

```
%%LST DDNTIMEOUTCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
        用户延时删除开关  =  使能
延时定时器时长下限值(分钟) =  30
延时定时器时长上限值(分钟) =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DDN定时器超时参数（LST-DDNTIMEOUTCTRL）_46314492.md`
