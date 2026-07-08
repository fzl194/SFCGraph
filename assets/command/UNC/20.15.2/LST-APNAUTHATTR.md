---
id: UNC@20.15.2@MMLCommand@LST APNAUTHATTR
type: MMLCommand
name: LST APNAUTHATTR（查询APN鉴权属性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNAUTHATTR
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN鉴权属性
status: active
---

# LST APNAUTHATTR（查询APN鉴权属性配置）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询APN鉴权属性配置信息。例如接入模式、鉴权模式、AAA鉴权服务器无响应处理开关等。

## 注意事项

当使用EXP MML命令导出密钥字段时，因本命令密钥参数“PASSWORD”是必选参数，系统会将其置为空，会导致报错，报错结果会在EXP MML命令导出的ERROR日志文件中。为使导出结果正常，需要在执行EXP MML命令前先执行MOD EXPCFGPARA命令，修改PWDKEY为omu的密码，并且在执行EXP MML命令时将PWDENCRPT参数设置为false，选择非匿名化。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNAUTHATTR]] · APN鉴权属性配置（APNAUTHATTR）

## 使用实例

- 假设用户要查询所有APN下配置的鉴权属性配置信息：
  ```
  %%LST APNAUTHATTR:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称               接入模式    鉴权模式  鉴权密码  PCO优先级  二次鉴权  公用用户名  公用密码  COA开关  DM开关  AAA鉴权服务器无响应处理  AAA Bypass后在线保持时长(分钟)  随机延迟范围(分钟)  使用PCO中的密码  Virtual Gi Id开关  Virtual Gi Id值  User Name信元填充方式  APN EAP鉴权  控制是否使用UDM签约数据参与决策进行AAA鉴权  控制是否使用UDM签约的AAA地址  控制2/3/4G场景下是否进行鉴权  控制AAA鉴权服务器回复Access Reject时是否允许用户继续激活  控制在二次鉴权流程中AAA未响应鉴权请求时Bypass会话是否插入ULCL  控制在二次鉴权流程中AAA回复reject时Bypass会话是否插入ULCL  控制UDM签约数据中未携带secondaryAuth信元时是否进行AAA鉴权

  0168apn1.com          透明不鉴权  使用PCO   *****     不使能     不使能    NULL        *****     不使能   使能    去活                     0                               0                   不使能           不使能             0                MSISDN                 不使能       不使能                                      不使能                        使能                          去活                                                      支持                                                           不支持		使能                                                     
  0168apn2.com          透明不鉴权  使用PCO   *****     不使能     不使能    NULL        *****     不使能   使能    去活                     0                               0                   不使能           不使能             0                MSISDN                 不使能       不使能                                      不使能                        使能                          去活                                                      支持                                                           不支持		使能                                                     
  a.mnc003.mcc460.gprs  透明不鉴权  使用PCO   *****     不使能     不使能    NULL        *****     不使能   使能    去活                     0                               0                   不使能           不使能             0                MSISDN                 不使能       不使能                                      不使能                        使能                          去活                                                      支持                                                           不支持		使能                                                     
  apn1                  透明不鉴权  使用PCO   *****     不使能     不使能    NULL        *****     不使能   使能    不去活                   0                               0                   不使能           不使能             0                MSISDN                 不使能       不使能                                      不使能                        使能                          不去活                                                    支持                                                           支持		使能                                                       
  huawei.com            透明不鉴权  使用PCO   *****     不使能     不使能    NULL        *****     不使能   使能    去活                     0                               0                   不使能           不使能             0                MSISDN                 不使能       不使能                                      不使能                        使能                          去活                                                      支持                                                           不支持		使能                                                     
  (结果个数 = 5)

  ---    END
  ```
- 假如运营商需要查询指定APN名为“apn1”的鉴权属性配置信息，则使用该实例：
  ```
  %%LST APNAUTHATTR: APN="apn1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                                        APN名称  =  apn1
                                                       接入模式  =  透明不鉴权
                                                       鉴权模式  =  使用PCO
                                                       鉴权密码  =  *****
                                                      PCO优先级  =  不使能
                                                       二次鉴权  =  不使能
                                                     公用用户名  =  NULL
                                                       公用密码  =  *****
                                                        COA开关  =  不使能
                                                         DM开关  =  使能
                                        AAA鉴权服务器无响应处理  =  不去活
                                 AAA Bypass后在线保持时长(分钟)  =  0
                                             随机延迟范围(分钟)  =  0
                                                使用PCO中的密码  =  不使能
                                              Virtual Gi Id开关  =  不使能
                                                Virtual Gi Id值  =  0
                                          User Name信元填充方式  =  MSISDN
                                                    APN EAP鉴权  =  不使能
                     控制是否使用UDM签约数据参与决策进行AAA鉴权  =  不使能
                                   控制是否使用UDM签约的AAA地址  =  不使能
                                   控制2/3/4G场景下是否进行鉴权  =  使能
       控制AAA鉴权服务器回复Access Reject时是否允许用户继续激活  =  不去活
  控制在二次鉴权流程中AAA未响应鉴权请求时Bypass会话是否插入ULCL  =  支持
      控制在二次鉴权流程中AAA回复reject时Bypass会话是否插入ULCL  =  支持
      控制UDM签约数据中未携带secondaryAuth信元时是否进行AAA鉴权  =  使能
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNAUTHATTR.md`
