---
id: UNC@20.15.2@MMLCommand@ADD GAISOLATION
type: MMLCommand
name: ADD GAISOLATION（增加Ga业务隔离配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GAISOLATION
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 业务隔离
status: active
---

# ADD GAISOLATION（增加Ga业务隔离配置）

## 功能

![](增加Ga业务隔离配置（ADD GAISOLATION）_63762720.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行RST RU生效。隔离正常运行中的AP模块，需要先执行STP CDRRECEIVE命令停止话单接收。添加隔离配置会导致隔离AP停止接收话单并禁止链路迁入。

**适用NF：NCG**

该命令用于隔离AP模块上的234G话单业务，即禁止Ga接口的接收话单，使得被隔离的AP不生成234G话单文件，并且禁止隔离AP上Ga链路的新建或迁入。

## 注意事项

- 最多可配置128条记录。
- 运行中的AP模块执行添加Ga业务隔离配置命令之前，需要执行**[**SET SRVSTH**](../../业务系统管理/业务功能开关/设置业务功能开关（SET SRVSTH）_41302357.md)**命令关闭负载均衡开关，通过链路迁移命令，将要隔离AP上的链路均衡迁移到其他234G业务AP上，执行[**STP CDRRECEIVE**](../../业务系统管理/话单接收管理/停止接收话单（STP CDRRECEIVE）_51174326.md)命令，停止NCG接收话单。
- 当用户增加了Ga隔离配置时，满足输入参数的234G业务AP模块，产生[**ALM-82014停止接收话单**](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82014 停止接收话单_51174189.md)告警。
- 若被隔离的AP存在未迁移的Ga链路，相关链路的业务将会切到备NCG并且上游网元会上报“**[**ALM-81021 CG无响应**](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81021 CG无响应_14905555.md)**”告警。
- 命令操作后，存在隔离配置的234G业务AP禁止Ga链路迁入。
- 命令操作后需要执行[**RST RU**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/重启资源单元（RST RU）_59103467.md)命令重启RU生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GAISOLATIONID | Ga隔离标识 | 可选必选说明：必选参数<br>参数含义：话单存储对象标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数只能由字母、数字、下划线、中划线组成。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| MNAME | 模块名称 | 可选必选说明：可选参数<br>参数含义：用于标识一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 该值需要执行<br>[**LST MODULE**](../业务模块/查询业务模块（LST MODULE）_51174292.md)<br>命令，查询出存在的“模块名称”进行填写。<br>- 不能输入的特殊字符请参考“<br>[**特殊字符表**](../话单备份/增加话单备份（ADD CDRBACKUP）_51174244.md#ZH-CN_CONCEPT_0251174244__table_0365FEF0)<br>”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GAISOLATION]] · Ga业务隔离配置（GAISOLATION）

## 使用实例

增加一个AP65_1的Ga口接入隔离，示例如下：

- 场景一：扩容RU65后，添加模块AP65_1前，添加Ga隔离配置。
  ```
  ADD GAISOLATION:GAISOLATIONID="iso1", MNAME="AP65_1";
  ```
- 场景二：运行中的AP65_1添加Ga隔离配置。
    - 关闭负载均衡开关
      ```
      SET SRVSTH: LINKSWITCH=OFF;
      ```
    - 通过链路迁移命令手动迁出AP65_1的Ga链路
      ```
      DSP ACTRL:;
      ```
      查询Ga链路状态。
      ```
      DSP RU: SERVICEINSTANCE="CG_VNFC_999";
      ```
      获取RU65的RU名称
      ```
      OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="crms spu-group", SERVICEINSTANCE="CG_VNFC_999";
      ```
      ```
      RETCODE = 0  操作成功  
      结果如下 
      --------                   
                        RU名称  =  CG_SP_RU2_0065               
                    SG进程ID号  =  1           
                调试命令字符串  =  crms spu-group 
      调试命令执行结果返回信息  =   spu-group 1  
      MasterSlot: 65  
      SlaveSlot: 64   
      Slot No.       Status              ElectionWght         
      - - - - - - - - - - - - - - - - - - - - - - - -  
      64             Normal              Normal               
      65             Normal              Normal                
      (结果个数 = 1)  
      ---    END
      ```
      ```
      OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="vcg show link 1", SERVICEINSTANCE="CG_VNFC_999";
      ```
      查询RU65上的前100条链路信息，此处的RUNAME为查出的MasterSlot RU编号对应的RU名称。
      ```
      OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="vcg operate move 1 641", SERVICEINSTANCE="CG_VNFC_999";
      ```
      将AP65_1上的Link Id为1的链路迁出到234G业务模块AP64_1上去。若AP65_1上还存在其它链路，通过该操作将AP65_1上的其它Ga链路全部迁出。
    - AP65_1停止接收234G话单
      ```
      STP CDRRECEIVE: MNAME="AP65_1";
      ```
    - AP65_1添加Ga隔离配置
      ```
      ADD GAISOLATION:GAISOLATIONID="iso1", MNAME="AP65_1";
      ```
    - 执行RST RU重启RU65
      ```
      RST RU: RUNAME="CG_SP_RU2_0065", SERVICEINSTANCE="CG_VNFC_999";
      ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Ga业务隔离配置（ADD-GAISOLATION）_63762720.md`
