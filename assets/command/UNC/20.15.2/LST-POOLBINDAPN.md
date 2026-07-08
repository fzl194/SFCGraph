---
id: UNC@20.15.2@MMLCommand@LST POOLBINDAPN
type: MMLCommand
name: LST POOLBINDAPN（查询APN实例与地址池绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLBINDAPN
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池绑定APN
status: active
---

# LST POOLBINDAPN（查询APN实例与地址池绑定关系）

## 功能

**适用NF：SMF**

该命令用来显示APN实例与地址池的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN/DNN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLBINDAPN]] · APN实例与地址池绑定关系（POOLBINDAPN）

## 使用实例

查询指定的APN与地址池的绑定信息，“APN”为“huawei.com”，“POOLNAME”为“lap”：

```
LST POOLBINDAPN:APN="huawei.com",POOLNAME="lap";
RETCODE = 0  操作成功。

地址池绑定APN配置信息
---------------------
 地址池名称  =  lap
    APN名称  =  huawei.com
     优先级  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POOLBINDAPN.md`
