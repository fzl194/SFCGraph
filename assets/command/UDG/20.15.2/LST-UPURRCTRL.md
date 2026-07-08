---
id: UDG@20.15.2@MMLCommand@LST UPURRCTRL
type: MMLCommand
name: LST UPURRCTRL（查询URR控制参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPURRCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- URR控制参数
status: active
---

# LST UPURRCTRL（查询URR控制参数）

## 功能

**适用NF：PGW-U、UPF**

查询URR控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPURRCTRL]] · URR控制参数（UPURRCTRL）

## 使用实例

查询URR控制参数：

```
LST UPURRCTRL:;
```

```

RETCODE = 0  操作成功

URR控制参数
----------------------
                    QHT上报时UPF是否删除URR开关  =  是
                      上报用量为空的URR消息类型  =  上报请求消息
              被聚合的URR用量为空时是否强制上报  =  是
                URR暂停测量期间是否触发费率切换  =  是
是否支持PDR关联未通过PFCP消息创建的预定义URR开关 =  否
(结果数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPURRCTRL.md`
