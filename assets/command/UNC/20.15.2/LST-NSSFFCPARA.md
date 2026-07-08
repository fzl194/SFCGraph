---
id: UNC@20.15.2@MMLCommand@LST NSSFFCPARA
type: MMLCommand
name: LST NSSFFCPARA（查询流控等级对应的流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFFCPARA
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# LST NSSFFCPARA（查询流控等级对应的流控参数）

## 功能

**适用NF：NSSF**

该命令用于查询流控等级对应的流控响应。

若要查询全部流控等级和对应的流控响应时，请不要输入任何参数。

若要查询特定流控等级或流控响应的相关信息时，请输入对应参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCLEVEL | 流控等级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示CPU过载程度的分级。<br>数据来源：本端规划<br>取值范围：<br>- “LOW（轻度过载）”：轻度过载对应的CPU阈值范围为大于等于75%、小于80%。<br>- “MEDIUM（中度过载）”：中度过载对应的CPU阈值范围为大于等于80%、小于85%。<br>- “HIGH（重度过载）”：重度过载对应的CPU阈值范围为大于等于85%、小于100%。<br>默认值：无<br>配置原则：无 |
| FCRSP | 流控响应 | 可选必选说明：可选参数<br>参数含义：该参数表示NSSF对流控等级的响应。<br>数据来源：本端规划<br>取值范围：<br>- “TooManyRequest_429（请求过多）”：NSSF收到NF的服务发现请求后直接回复响应，错误码为429。<br>- “ServiceUnavailable_503（服务不可用）”：NSSF收到NF的服务发现请求后直接回复响应，错误码为503。<br>- “NoResponse（无响应）”：NSSF收到NF的服务发现请求后直接将消息丢弃。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFFCPARA]] · 流控等级对应的流控参数（NSSFFCPARA）

## 使用实例

- 当运营商希望查询所有流控等级对应的流控响应时，执行此命令：
  ```
  LST NSSFFCPARA:;
  %%LST NSSFFCPARA:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  流控等级  流控响应  

  轻度过载  无响应        
  中度过载  无响应     
  重度过载  无响应             
  (结果个数 = 3)
  ```
- 当运营商希望查询流控等级为轻度过载对应的流控响应信息时，执行此命令：
  ```
  LST NSSFFCPARA: FCLEVEL=LOW;
  %%LST NSSFFCPARA: FCLEVEL=LOW;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
     流控等级  =  轻度过载
     流控响应  =  无响应
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSFFCPARA.md`
