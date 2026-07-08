---
id: UNC@20.15.2@MMLCommand@LST NONIPSUBCTRL
type: MMLCommand
name: LST NONIPSUBCTRL（查询Non-IP APNNI配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NONIPSUBCTRL
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
- M2M管理
- Non-IP APNNI配置
status: active
---

# LST NONIPSUBCTRL（查询Non-IP APNNI配置）

## 功能

**适用网元：MME**

该命令用于查询Non-IP APNNI配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NONIPSUBCTRL]] · Non-IP APNNI配置（NONIPSUBCTRL）

## 使用实例

查询所有Non-IP APNNI的配置：

LST NONIPSUBCTRL:;

```
%%LST NONIPSUBCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
         用户范围  =  所有用户
         IMSI前缀  =  NULL
支持Non-IP的APNNI  =  所有APNNI
        APNNI组号  =  NULL
        缺省APNNI  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NONIPSUBCTRL.md`
