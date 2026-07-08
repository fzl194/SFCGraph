---
id: UNC@20.15.2@MMLCommand@MOD SCTPLE
type: MMLCommand
name: MOD SCTPLE（修改SCTP本地实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCTPLE
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体
status: active
---

# MOD SCTPLE（修改SCTP本地实体）

## 功能

**适用网元：MME、AMF**

此命令用于修改SCTP本端实体的配置参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令可修改该SCTP本端实体的用途、权重、SCTP参数索引、是否开启交叉路径和描述。

## 权限

manage-ug; system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPLEIDX | SCTP本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本端实体索引用于唯一标识一个SCTP本端实体。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1023。<br>默认值：无 |
| CROSSIPFLG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的交叉路径是否可用选择为否时表示交叉路径不开启，选择为是时表示开启交叉路径。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- E_SCTP_CROSS_NO：交叉路径不可用<br>- E_SCTP_CROSS_YES：交叉路径可用<br>默认值：无 |
| SCTPPARAIDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的参数配置索引，用于根据该索引获取到SCTP协议的参数配置信息该参数通过ADD SCTPPARA命令配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~65534。<br>默认值：无 |
| USAGE | 用途 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的使用者信息，协议中定义了不同偶联可指定给不同类型的用户使用，如可指定使用者为UE、NON-UE或BOTH。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- E_SCTP_USAGE_UE：用于指定SCTP本端实体的使用者<br>- E_SCTP_USAGE_NONUE<br>- E_SCTP_USAGE_BOTH<br>默认值：无 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的权重如果该值设置为0，则标识NGAP初始化消息不允许使用该SCTP本端实体，如果该值多个SCTP本端实体设置一样，则标识在多个SCTP本端实体间负载均衡。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无<br>说明：该参数对SFGAP不生效。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的描述信息。<br>数据来源：<br>取值范围：字符串类型，输入长度范围为0~31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLE]] · SCTP本地实体（SCTPLE）

## 使用实例

将链路本地实体索引为1的SCTP链路的用户类型改为UE:

```
%%MOD SCTPLE: SCTPLEIDX=1, USAGE=E_SCTP_USAGE_UE;%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SCTPLE.md`
