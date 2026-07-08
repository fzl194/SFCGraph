---
id: UNC@20.15.2@MMLCommand@OPR ONECLICKDEPLOY
type: MMLCommand
name: OPR ONECLICKDEPLOY（操作服务一键式部署）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: ONECLICKDEPLOY
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# OPR ONECLICKDEPLOY（操作服务一键式部署）

## 功能

![](操作服务一键式部署（OPR ONECLICKDEPLOY）_93911016.assets/notice_3.0-zh-cn_2.png)

堆栈下线和服务下线功能会将已启用的服务下线，该服务将不会接受相关业务。

该命令用于操作网元一键式部署任务。

## 注意事项

如果命令下发返回超时，请通过 [**DSP ONECLICKDEPLOYHIST**](显示一键式部署操作历史（DSP ONECLICKDEPLOYHIST）_93751500.md) 查询执行结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPRTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示一键式部署任务的操作类型。<br>数据来源：本端规划<br>取值范围：<br>- INDEPSTACKENABLE（独立堆栈服务上线）<br>- INDEPSTACKDISABLE（独立堆栈服务下线）<br>- FEATUREENABLE（主堆栈服务上线）<br>- FEATUREDISABLE（主堆栈服务下线）<br>- SCALEOUT（服务扩容）<br>- SCALEIN（服务缩容）<br>- DELETE（删除）<br>- RETRY（重试）<br>- ROLLBACK（回退）<br>默认值：无<br>配置原则：无 |
| NODETYPELIST | 节点类型列表 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"INDEPSTACKDISABLE"、"FEATUREENABLE"、"FEATUREDISABLE"、"SCALEOUT"、"SCALEIN"时为条件可选参数。<br>参数含义：该参数用于表示一键式部署任务的操作的节点信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| PODTYPELIST | Pod类型列表 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"时为条件必选参数。该参数在"OPRTYPE"配置为"SCALEOUT"、"SCALEIN"时为条件可选参数。<br>参数含义：该参数用于表示一键式部署任务的操作的Pod信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。输入格式如下："podtype1:podnum1/podtype2:podnum2"。<br>默认值：无<br>配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"、"FEATUREDISABLE"时为条件必选参数。<br>参数含义：该参数用于表示一键式部署任务的操作的网络功能集名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| VMNAMELIST | 虚机名称列表 | 可选必选说明：该参数在"OPRTYPE"配置为"DELETE"时为条件必选参数。<br>参数含义：该参数用于标识需要缩容的虚机名称列表。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。输入格式如下："VmName1/VmName2"。<br>默认值：无<br>配置原则：<br>该参数仅在虚机场景下使用。 |
| MEID | 网元ID | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"INDEPSTACKDISABLE"、"FEATUREENABLE"、"FEATUREDISABLE"、"SCALEOUT"、"SCALEIN"、"DELETE"时为条件可选参数。<br>参数含义：该参数用于表示一键式部署任务的网元标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| EXTENDEDATTR | 扩展属性 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"时为条件可选参数。<br>参数含义：该参数为预留功能，无需填写。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| PKGNAME | 软件包名称 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"时为条件必选参数。<br>参数含义：该参数用于表示一键式部署任务的操作的软件包名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。该参数可以通过DSP VNFPKGS的返回值中获取。<br>默认值：无<br>配置原则：无 |
| INPUT | 模板INPUT参数 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"时为条件可选参数。<br>参数含义：该参数用于表示一键式部署任务的需要更新的模板输入参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~512。输入格式如下："key1:value1/key2:value2"。<br>默认值：无<br>配置原则：无 |
| PROCESSTYPE | 处理方式 | 可选必选说明：该参数在"OPRTYPE"配置为"FEATUREDISABLE"时为条件必选参数。<br>参数含义：该参数用于指定服务下线方式：<br>若选择普通下线，内部流程异常时下线任务会终止，修复问题后可以重新下发下线任务；<br>若选择强制下线，内部流程异常时也会强制将服务下线。强制下线是高危命令，建议操作该动作时，寻求研发工程师支持。<br>数据来源：本端规划<br>取值范围：<br>- Normal（普通操作）<br>- Force（强制操作）<br>默认值：无<br>配置原则：无 |
| STACKNAME | 堆栈名称 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKDISABLE"时为条件必选参数。<br>参数含义：该参数用于标识堆栈名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。该参数可以通过DSP VNFSTACKNAMES的返回值中获取。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ONECLICKDEPLOY]] · 操作服务一键式部署（ONECLICKDEPLOY）

## 使用实例

假如运营商需要上线UDG-to堆栈，可以通过调用以下命令进行堆栈上线。

```
%%OPR ONECLICKDEPLOY: OPRTYPE=INDEPSTACKENABLE, PODTYPELIST="to-pod:1/toctrl-pod:1", FUNCTIONSETNAME="UDG-to", PKGNAME="unc-to-24.1.rc1.b061-tosca-std-edge-arm", INPUT="appprogress:false";%%
RETCODE = 0  操作成功

结果如下
--------
接受结果  =  accepted
结果说明  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-ONECLICKDEPLOY.md`
