---
id: UDG@20.15.2@MMLCommand@LST RELAYTESTUSER
type: MMLCommand
name: LST RELAYTESTUSER（查询媒体中继拨测用户）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYTESTUSER
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
- 媒体中继拨测用户配置
status: active
---

# LST RELAYTESTUSER（查询媒体中继拨测用户）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继拨测用户。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TESTUSERNAME | 拨测用户名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYTESTUSER]] · 媒体中继拨测用户（RELAYTESTUSER）

## 使用实例

查询媒体中继拨测用户：

```
LST RELAYTESTUSER:TESTUSERNAME="user01";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
	拨测用户名称	=  user01
		APN名称	=  apn
		用户类型	=  IMSI
		   IMSI =  460011223344551
 媒体中继功能开关  =  Enable
	用户模板名称	=  profile01
	 配置域名称   =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYTESTUSER.md`
