---
id: UNC@20.15.2@MMLCommand@LST SCEF
type: MMLCommand
name: LST SCEF（查询SCEF配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCEF
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- SCEF管理
status: active
---

# LST SCEF（查询SCEF配置）

## 功能

**适用网元：MME**

该命令用于查询SCEF配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCEFRLM | SCEF域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCEF域名。<br>数据来源：对端协商<br>取值范围：1~127位字符串<br>默认值：无 |
| SCEFHTN | SCEF主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCEF主机名。<br>数据来源：对端协商<br>取值范围：1~127位字符串<br>默认值：无 |

## 操作的配置对象

- [SCEF配置（SCEF）](configobject/UNC/20.15.2/SCEF.md)

## 使用实例

查询SCEF配置：

LST SCEF:;

```
%%LST SCEF:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  SCEF域名  =  huawei01.com
SCEF主机名  =  scef0701.huawei01.com
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCEF配置(LST-SCEF)_72345057.md`
