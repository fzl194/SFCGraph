# 查询NG-RAN基站邻接关系配置（LST NGRANNEIBCFG）

- [命令功能](#ZH-CN_MMLREF_0209652382__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652382__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652382__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652382__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652382__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652382)

**适用NF：AMF**

此命令用于查询中手动添加的NG-RAN基站邻接关系。

## [注意事项](#ZH-CN_MMLREF_0209652382)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652382)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652382)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心基站和邻接基站公用的基站类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：可选参数<br>参数含义：该参数标识接入网设备的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRANNODEID | NG-RAN基站标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心NG-RAN基站的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。如果NGRANNODETYPE设置为GNB，则该参数的值范围为0到4294967295；如果NGRANNODETYPE设置为MACRONGENB，则该参数的值范围为0到1048575；如果将NGRANNODETYPE设置为SHORTNGENB，则该参数的取值范围为0到262143；如果将NGRANNODETYPE设置为LONGNGENB，则该参数的取值范围为0到2097151；如果NGRANNODETYPE被设置为N3IWF，则该参数的值范围从0到65535。<br>默认值：无<br>配置原则：无 |
| NODEIDLEN | NG-RAN基站标识长度(比特) | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心NG-RAN基站和邻接基站共用的标识长度(比特)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是16~32。当NGRANNODETYPE选择GNB时，本参数的输入范围应当是22到32；当NGRANNODETYPE选择MACRONGENB时，本参数应当输入值为20；当NGRANNODETYPE选择SHORTNGENB时，本参数应当输入值为18；当NGRANNODETYPE选择LONGNGENB时，本参数应当输入值为21；当NGRANNODETYPE选择N3IWF时，本参数应当输入值为16。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652382)

- 查询“NG-RAN基站类型”为“Global gNB”的NG-RAN基站邻接关系，执行如下命令：
  ```
  %%LST NGRANNEIBCFG: NGRANNODETYPE=GNB;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NG-RAN基站类型  =  Global gNB
                      PLMN  =  12303
            NG-RAN基站标识  =  327697
  NG-RAN基站标识长度(比特)  =  24
    邻接NG-RAN基站标识列表  =  327696&327698&327699
  (结果个数 = 1)

  ---    END
  ```
- 查询所有手动添加的NG-RAN基站邻接关系，执行如下命令：
  ```
  %%LST NGRANNEIBCFG:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NG-RAN基站类型  =  Global gNB
                      PLMN  =  12303
            NG-RAN基站标识  =  327697
  NG-RAN基站标识长度(比特)  =  24
    邻接NG-RAN基站标识列表  =  327696&327698&327699
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209652382)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NG-RAN基站类型 | 该参数用于指定中心基站和邻接基站公用的基站类型。 |
| PLMN | 该参数标识接入网设备的PLMN信息。 |
| NG-RAN基站标识 | 该参数用于指定中心NG-RAN基站的标识。 |
| NG-RAN基站标识长度(比特) | 该参数用于指定中心NG-RAN基站和邻接基站共用的标识长度(比特)。 |
| 邻接NG-RAN基站标识列表 | 该参数用于指定邻接NG-RAN基站列表，建立中心NG-RAN基站及其周边基站的邻接关系。 |
