---
id: UDG@20.15.2@MMLCommand@LST RELAYHTTPMHD
type: MMLCommand
name: LST RELAYHTTPMHD（查询媒体中继HTTP消息头）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYHTTPMHD
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继HTTP消息头
status: active
---

# LST RELAYHTTPMHD（查询媒体中继HTTP消息头）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继HTTP消息头。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTTPMSGCTRLNAME | HTTP消息控制名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP消息控制名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYHTTPMCTL命令配置生成。<br>- 该取值必须和ADD RELAYHTTPMCTL中配置的"HTTPMAGCTRLNAME"参数取值相同。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYHTTPMHD]] · 媒体中继HTTP消息头（RELAYHTTPMHD）

## 使用实例

查询媒体中继HTTP消息头：

```
LST RELAYHTTPMHD:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
HTTP消息头名称  =  http01
      消息类型  =  UE HTTP响应
      头域名称  =  Age
       头域值  =  100
         描述  =  NULL
    配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYHTTPMHD.md`
