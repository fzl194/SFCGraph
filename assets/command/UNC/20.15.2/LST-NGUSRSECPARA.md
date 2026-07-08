---
id: UNC@20.15.2@MMLCommand@LST NGUSRSECPARA
type: MMLCommand
name: LST NGUSRSECPARA（查询5G用户安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGUSRSECPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 用户安全参数管理
status: active
---

# LST NGUSRSECPARA（查询5G用户安全配置）

## 功能

**适用NF：AMF**

此命令用于查询指定用户的鉴权、加密、完整性保护等安全配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置安全参数的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “IMSI_PREFIX（指定IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于系统根据指定用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G用户安全配置（NGUSRSECPARA）](configobject/UNC/20.15.2/NGUSRSECPARA.md)

## 使用实例

查询用户范围为所有用户的安全参数配置，执行如下命令：

```
%%LST NGUSRSECPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
   用户范围  =  所有用户
   IMSI前缀  =  NULL
 完整性算法  =  SNOW 3G完整性算法&AES完整性算法&ZUC完整性算法
   加密算法  =  空加密算法&SNOW 3G加密算法&AES加密算法&ZUC加密算法
   鉴权事件  =  初始注册&移动性INTER注册&空闲态EPS到5GS注册
   描述信息  =  NULL
鉴权周期(h)  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G用户安全配置（LST-NGUSRSECPARA）_09651449.md`
