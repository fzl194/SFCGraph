---
id: UNC@20.15.2@MMLCommand@LST AMFEVENTCMPT
type: MMLCommand
name: LST AMFEVENTCMPT（查询事件订阅通知消息的兼容性控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFEVENTCMPT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 事件订阅接口管理
- AMF事件订阅兼容性参数管理
status: active
---

# LST AMFEVENTCMPT（查询事件订阅通知消息的兼容性控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF事件订阅的兼容性控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFEVENTCMPT]] · 事件订阅通知消息的兼容性控制参数（AMFEVENTCMPT）

## 使用实例

查询AMF事件订阅的兼容性参数，执行如下命令。

```
%%LST AMFEVENTCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
UE当前驻留的基站全局标识  =  No
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询事件订阅通知消息的兼容性控制参数（LST-AMFEVENTCMPT）_57869699.md`
