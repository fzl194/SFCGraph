---
id: UNC@20.15.2@MMLCommand@LST HTTPSTATPARA
type: MMLCommand
name: LST HTTPSTATPARA（查询HTTP统计参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPSTATPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP链路内部统计管理
status: active
---

# LST HTTPSTATPARA（查询HTTP统计参数）

## 功能

该命令用于查询进行统计的HTTP对端地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIPTYPE | 对端IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP统计参数（HTTPSTATPARA）](configobject/UNC/20.15.2/HTTPSTATPARA.md)

## 使用实例

查询HTTP统计的对端IP地址，执行命令如下：

```
%%LST HTTPSTATPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
对端IP地址类型  对端IPv4地址  对端IPv6地址        

IPv4            10.2.3.4      ::
IPv4            10.2.3.5      ::
IPv4            10.2.3.6      ::
IPv4            10.2.3.7      ::
IPv4            10.2.3.8      ::
IPv4            10.2.3.9      ::
IPv4            10.2.3.10     ::
(结果个数 = 7)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP统计参数（LST-HTTPSTATPARA）_83972188.md`
