---
id: UNC@20.15.2@MMLCommand@LST NGVOICEDEPLOY
type: MMLCommand
name: LST NGVOICEDEPLOY（查询5G语音部署配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGVOICEDEPLOY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- VoPS管理
status: active
---

# LST NGVOICEDEPLOY（查询5G语音部署配置）

## 功能

**适用NF：AMF**

该命令用于查询UE使用5G网络接入时的IMS VoPS语音部署策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用语音策略用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGVOICEDEPLOY]] · 5G语音部署配置（NGVOICEDEPLOY）

## 使用实例

查询本网用户语音部署配置，执行如下命令：

```
%%LST NGVOICEDEPLOY: SUBRANGE=HOME_USER;%%
RETCODE = 0  操作成功

结果如下
------------------------
                    用户范围  =  本网用户
                    IMSI前缀  =  NULL
          AMF是否支持IMS语音  =  不支持
Data Centric类型终端支持VoPS  =  不支持
      是否检查用户S1Mode能力  =  关闭
                 语音业务DNN  =  1.1
检查语音DNN是否支持EPS互操作  =  关闭
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGVOICEDEPLOY.md`
