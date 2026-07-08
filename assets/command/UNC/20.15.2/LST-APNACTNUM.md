---
id: UNC@20.15.2@MMLCommand@LST APNACTNUM
type: MMLCommand
name: LST APNACTNUM（查询APN激活数目限制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNACTNUM
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APN激活数目限制配置
status: active
---

# LST APNACTNUM（查询APN激活数目限制）

## 功能

**适用网元：MME**

该命令用于查询APN激活数目限制的配置记录。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDN连接建立流程中使用的APN网络标识。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾<br>说明：“*”为通配符，表示对所有的APNNI生效。如果不输入该参数，则表示查询系统内所有APN激活数目限制的配置记录 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNACTNUM]] · APN激活数目限制（APNACTNUM）

## 使用实例

查询所有APN激活限制数目的配置记录：

LST APNACTNUM:;

```
%%LST APNACTNUM:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
                 APN网络标识  =  HUAWEI
                 PDN连接数目  =  2
                IPv4地址数目  =  2
                IPv6地址数目  =  2
             PDN连接拒绝原因  =  Operator Determined Barring 8
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNACTNUM.md`
