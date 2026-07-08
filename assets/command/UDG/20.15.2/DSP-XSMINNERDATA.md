---
id: UDG@20.15.2@MMLCommand@DSP XSMINNERDATA
type: MMLCommand
name: DSP XSMINNERDATA（显示XSM模块与其他模块的组件间交互消息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: XSMINNERDATA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP XSMINNERDATA（显示XSM模块与其他模块的组件间交互消息）

## 功能

该命令用于显示XSM模块与其他模块的组件间交互消息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CID | 组件ID | 可选必选说明：必选参数<br>参数含义：与XSM进行消息交互的组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。<br>默认值：无 |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLACKBOX：黑盒信息。<br>- WORKSPACE：工作空间信息。<br>- DATAMDLFAIL：数据模型失败信息。<br>- SCHEMAMAPFAIL：模型映射失败信息。<br>- FAILOPER：操作失败信息。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/XSMINNERDATA]] · XSM模块与其他模块的组件间交互消息（XSMINNERDATA）

## 使用实例

- 显示XSM模块与其他模块的组件间交互消息：
  ```
  DSP XSMINNERDATA:CID="82080022",DATATYPE=WORKSPACE
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  输出字符串  =  Work-Space 1 Info:
  Create Time            :2016-06-02 12:34:56:900
  Decode Call Num        :123
  Decode Continue Num    :0
  Encode Num             :8193
  Encode Continue Num    :0
  OperLog Call Num       :0
  Update User Proc       :1
  WithType               :FALSE
  AuthEnabled            :TRUE
  Last OperLog String    :/netconf/NcsXsmInnerDatas
  Denied operations      :0
  Denied access write    :0
  (结果个数 = 1)
  ---    END
  ```
- 显示XSM模块黑盒信息：
  ```
  DSP XSMINNERDATA:CID="82080022",DATATYPE=BLACKBOX
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  错误消息字符串  =  27/22:56:21:449 query     /netconf/XsmInnerDatas  invalid xml content                                                                                                              
  (结果个数 = 1)
  ---    END
  ```
- 显示XSM模块操作失败信息：
  ```
  DSP XSMINNERDATA:CID="82080025",DATATYPE=FAILOPER
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  时间戳                 错误消息字符串                                                                                                                

  2016-12-22 19:17:04    Reason=Add response node to child error;ErrorCode=0x1;Oper=get;NcaErrorCode=0x14e;CfgErrorCode=0x0;TransId=0                       
  2016-12-22 19:36:35    Reason=Create new edit request CFG object block error;ErrorCode=0x1;Oper=edit-config;NcaErrorCode=0x14e;CfgErrorCode=0x0;TransId=11
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示XSM模块与其他模块的组件间交互消息（DSP-XSMINNERDATA）_59104187.md`
