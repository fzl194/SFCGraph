---
id: UDG@20.15.2@MMLCommand@LST UPTWTIMER
type: MMLCommand
name: LST UPTWTIMER（查询TW定时器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPTWTIMER
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter公共参数
status: active
---

# LST UPTWTIMER（查询TW定时器）

## 功能

**适用NF：UPF**

该命令用于查询Diameter TW定时器。

## 注意事项

该命令相关的功能当前版本暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [TW定时器（UPTWTIMER）](configobject/UDG/20.15.2/UPTWTIMER.md)

## 使用实例

查询Diameter TW定时器，则可按如下配置：

```
LST UPTWTIMER:;
```

```

RETCODE = 0  操作成功。
TW定时器配置
------------
      TW定时器时长（秒）  =  3
 DWR消息响应超时次数上限  =  3
超时次数达到上限复位连接  =  复位TCP
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TW定时器（LST-UPTWTIMER）_97080145.md`
