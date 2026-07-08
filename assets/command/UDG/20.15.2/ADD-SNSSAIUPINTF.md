---
id: UDG@20.15.2@MMLCommand@ADD SNSSAIUPINTF
type: MMLCommand
name: ADD SNSSAIUPINTF（增加网络切片和逻辑接口绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SNSSAIUPINTF
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: true
max_records: 8192
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片与逻辑接口绑定关系配置
status: active
---

# ADD SNSSAIUPINTF（增加网络切片和逻辑接口绑定关系）

## 功能

**适用NF：UPF**

![](增加网络切片和逻辑接口绑定关系（ADD SNSSAIUPINTF）_51061265.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令会导致切片用户使用的逻辑接口发生变化，可能会导致业务链路不通。

该命令用于给指定的网络切片选择标识绑定一个N3逻辑接口。

## 注意事项

- 该命令执行后，对新的PFCP消息生效。
- 该命令最大记录数为8192。
- 增加配置会导致切片用户选择的逻辑接口发生变化，可能会导致业务链路不通。
- 允许配置融合接口Saif。
- N3if1/1/0或者Saif1/1/0为默认的逻辑接口，不能绑定网络切片。建议环境上初始配置逻辑接口N3if1/1/0或者Saif1/1/0，当没有携带切片的会话需要选择N3逻辑接口时，至少可以选择到N3if1/1/0或者Saif1/1/0。
- 删除逻辑接口时，切片与被删除的逻辑接口的绑定关系将自动解绑。
- 数据面接口模式为INSTANCE时，不支持网络切片与逻辑接口绑定。
- MBS会话激活时，n3mbif接口不能绑定网络切片。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片/服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如果S-NSSAI无SD，需配置为全F。 |
| N3LOGICINF | N3逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置N3逻辑接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 逻辑接口类型：n3if，saif。<br>- ISU组号：1。<br>- ISU实例类型：1。1表示Instance级类型。<br>- 逻辑接口号：0~31。<br>- 该逻辑接口名称必须是通过ADD LOGICINF命令已经配置的。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SNSSAIUPINTF]] · 网络切片和逻辑接口绑定关系（SNSSAIUPINTF）

## 使用实例

- 假如运营商要给SST为1，SD为“123456”的S-NSSAI绑定逻辑接口n3if1/1/1：
  ```
  ADD SNSSAIUPINTF: SST=1, SD="123456", N3LOGICINF="n3if1/1/1";
  ```
- 假如运营商要给SST为1，SD为空的S-NSSAI绑定逻辑接口n3if1/1/1，真正设置的是SST为1，SD为"ffffff"的S-NSSAI绑定逻辑接口n3if1/1/1：
  ```
  ADD SNSSAIUPINTF: SST=1, N3LOGICINF="n3if1/1/1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SNSSAIUPINTF.md`
