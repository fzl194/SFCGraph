---
id: UNC@20.15.2@MMLCommand@RMV USER
type: MMLCommand
name: RMV USER（删除用户）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 用户管理
status: active
---

# RMV USER（删除用户）

## 功能

![](删除用户(RMV USER)_06404641.assets/notice_3.0-zh-cn_2.png)

该操作将删除用户，同时清除该用户所有信息。

本命令用于删除一个已创建的OM Portal用户。

## 注意事项

不支持删除默认用户。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| USRNAME | 用户名称 | 可选必选说明：必选参数。<br>参数含义：用户名称，可在OM Portal的“安全 > 用户管理”查询<br>取值范围：长度不超过32个字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [用户锁定状态（USER）](configobject/UNC/20.15.2/USER.md)

## 使用实例

删除用户test01：

```
%%RMV USER: USRNAME="test01";%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户(RMV-USER)_06404641.md`
