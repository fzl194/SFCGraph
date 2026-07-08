---
id: UNC@20.15.2@MMLCommand@LST RESULTCODESCP
type: MMLCommand
name: LST RESULTCODESCP（查询配置MODELC/D组网的SCP原因码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESULTCODESCP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# LST RESULTCODESCP（查询配置MODELC/D组网的SCP原因码）

## 功能

**适用NF：SMF、PGW-C、GGSN**

此命令用来查询指定组网场景结果码控制信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>如果配置为“global”则表示全局配置。<br>如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| MODELTYPE | 组网场景 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该返回码所应用的组网场景。<br>数据来源：本端规划<br>取值范围：<br>- “MODELC（组网场景为ModelC）”：组网场景为ModelC<br>- “MODELD（组网场景为ModelD）”：组网场景为ModelD。<br>- “MODELC_D（组网场景为ModelC和ModelD）”：组网场景为ModelC和ModelD。<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：可选参数<br>参数含义：本参数用于配置N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~3。300-599中的一个值或者3xx、4xx、5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| ERRINFO | 故障码对应的Protocol or application Error信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自定义的故障码对应的Protocol or application Error信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。如果配置为星号（*），表示通配，对该异常码携带所有Protocol or application Error信息都生效。参考3GPP协议29.500的Protocol or application Error。<br>默认值：无<br>配置原则：<br>（1）该参数只能由字母（A-Z或者a-z）、数字（0-9）、下划线（_）、星号（*）组成。该参数不区分大小写。<br>（2）配置为“*”，表示该异常码动作对于所有的Protocol or application Error信息都生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESULTCODESCP]] · 配置MODELC/D组网的SCP原因码控制（RESULTCODESCP）

## 使用实例

查询PCC模板为“pcctemplate”的SCP返回码控制信息：

```
%%LST RESULTCODESCP: PCCTEMPLATE="pcctemplate";%%
RETCODE = 0  操作成功

结果如下
--------
                                  PCC模板名称  =  pcctemplate
                                     组网场景  =  组网场景为ModelC
                                     N7返回码  =  502
故障码对应的Protocol or application Error信息  =  nf_failover
                          Initial流程处理动作  =  回滚为本地PCC用户使用本地策略
            Initial流程回滚后使能Holding-Time  =  不使能
                           Update流程处理动作  =  去活会话
             Update流程回滚后使能Holding-Time  =  不使能
                        Terminate流程处理动作  =  缺省动作
                                 重新激活请求  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESULTCODESCP.md`
