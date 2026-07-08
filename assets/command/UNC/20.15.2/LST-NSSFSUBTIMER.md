---
id: UNC@20.15.2@MMLCommand@LST NSSFSUBTIMER
type: MMLCommand
name: LST NSSFSUBTIMER（查询订阅时长）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFSUBTIMER
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF订阅时长管理
status: active
---

# LST NSSFSUBTIMER（查询订阅时长）

## 功能

**适用NF：NSSF**

该命令用于查询AMF订阅NSSF切片可用性服务的有效期时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于描述网元类型。<br>数据来源：全网规划<br>取值范围：<br>- AMF（接入和移动性管理网络功能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFSUBTIMER]] · 订阅时长（NSSFSUBTIMER）

## 使用实例

假如运营商希望查询所有已设置的订阅有效时长信息，执行下列命令。

```
LST NSSFSUBTIMER:;
%%LST NSSFSUBTIMER:;%%
RETCODE = 0  操作成功

结果如下
--------
    网元类型  =  接入和移动性管理网络功能
订阅有效时长(秒)  =  86400
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSFSUBTIMER.md`
