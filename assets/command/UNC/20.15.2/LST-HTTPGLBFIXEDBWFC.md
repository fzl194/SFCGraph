---
id: UNC@20.15.2@MMLCommand@LST HTTPGLBFIXEDBWFC
type: MMLCommand
name: LST HTTPGLBFIXEDBWFC（查询HTTP全局固定带宽流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPGLBFIXEDBWFC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP全局固定带宽流控管理
status: active
---

# LST HTTPGLBFIXEDBWFC（查询HTTP全局固定带宽流控）

## 功能

该命令用于查询HTTP全局固定带宽流控的门限值等信息。

## 注意事项

此命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [HTTP全局固定带宽流控（HTTPGLBFIXEDBWFC）](configobject/UNC/20.15.2/HTTPGLBFIXEDBWFC.md)

## 使用实例

查询HTTP全局固定带宽流控的门限值等信息，可以用以下命令：

```
LST HTTPGLBFIXEDBWFC:;
%%LST HTTPGLBFIXEDBWFC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                     全局固定带宽流控出局开关 = 开启 
                     全局固定带宽流控入局开关 = 开启
               发送消息带宽流控门限(千字节/s) = 15000
               接收消息带宽流控门限(千字节/s) = 15000
                     发送消息大包阈值(千字节) = 1024
                     接收消息大包阈值(千字节) = 1024
                                       状态码 = 太多请求
(结果 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP全局固定带宽流控（LST-HTTPGLBFIXEDBWFC）_03315070.md`
