---
id: UNC@20.15.2@MMLCommand@LST TWTIMER
type: MMLCommand
name: LST TWTIMER（查询TW定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TWTIMER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- Diameter公共参数
status: active
---

# LST TWTIMER（查询TW定时器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter TW定时器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/TWTIMER]] · TW定时器（TWTIMER）

## 使用实例

查询Diameter TW定时器，则可按如下配置：

```
LST TWTIMER:;
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

- 原始手册：`evidence/UNC/20.15.2/LST-TWTIMER.md`
