# 配置SMF和“UL CL UPF+辅锚点UPF”对接

- [操作场景](#ZH-CN_OPI_0231367702__1.3.1)
- [必备事项](#ZH-CN_OPI_0231367702__1.3.2)
- [操作步骤](#ZH-CN_OPI_0231367702__1.3.3)
- [任务示例](#ZH-CN_OPI_0231367702__1.3.4)

## [操作场景](#ZH-CN_OPI_0231367702)

本操作指导介绍部署基于预定义规则的分流策略控制特性的操作过程。

3GPP针对于5G用户面的数据分流定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。

当UE会话激活或位置发生变化时，SMF基于用户的DNN、位置区以及DNAI（Data Network Access Identifier）等信息判定是否需要将用户数据分流到本地DN，如需分流则为用户选择UL CL UPF和辅锚点UPF，将UL CL UPF和辅锚点UPF插入当前的会话中并对UL CL UPF下发相应的分流规则来实现对用户本地数据的分流控制。

> **说明**
> DNAI（DN Access Identifier）是3GPP定义用于标识DN网络接入点。DNN表示DN的名称，DNAI则表示DN的具体网络接入点，带有一定的物理属性。例如网络中规划了一个DN，其DNN为abc，该DN有A城和B城两个接入点，则A、B城对应的DNAI可以命名为abc.A和abc.B。在UL CL分流场景下，DNAI则用于标识边缘侧的PDU会话锚点，即辅锚点UPF。

如前所述本特性仅支持UL CL UPF和辅锚点UPF合一部署场景，前面原理描述中主锚点PSA0 UPF和“UL CL UPF+辅锚点UPF”是分离部署的。但是在现网实际使用过程中可能出现“UL CL UPF+辅锚点UPF”和主锚点PSA0 UPF共部署场景，华为SMF支持和这种UL CL和主、辅锚点UPF合一部署形态的UPF进行对接并实现UL CL分流，详细如 [表1](#ZH-CN_OPI_0231367702__table8545161651514) 所示。

*表1 SMF与UL CL和主、辅锚点UPF共部署形态的UPF的组网对接介绍*

| 场景 | 原理描述 |
| --- | --- |
| 为某工业园区建分流网络，希望最大限度节约成本，将UL CL和主、辅锚点UPF共部署。接入园区的用户访问公网以及本地DN都使用该合一形态的UPF。 | 此时SMF需要和UPF间创建两个N4会话，一个主锚点N4会话，一个辅锚点N4会话。UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。<br>SMF上需要打开<br>[**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md)<br>命令中<br>“ UPF共享开关”<br>才能使能该使用场景。同时还需要配置命令<br>**[ADD VIRTUALUPFID](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/DNAI绑定管理/增加虚拟UPF实例标识的DNAI（ADD VUPFIDBINDDNAI）_76311127.md)**<br>和<br>**[ADD VUPFIDBINDDNAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/DNAI绑定管理/增加虚拟UPF实例标识的DNAI（ADD VUPFIDBINDDNAI）_76311127.md)**<br>来指定辅锚点会话的DNAI。 |

## [必备事项](#ZH-CN_OPI_0231367702)

前提条件

请仔细阅读 [WSFD-108002 基于预定义规则的分流策略控制特性概述](特性概述_28859310.md) 特性原理概述。

数据

> **说明**
> 下表中“取值样例”列同色字体表示命令间的关联参数。

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 本端规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | NF类型（NFTYPE） | NfUPF | 本端规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | NF状态（NFSTATUS） | Registered | 本端规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | 域名（FQDN） | upf01.node.mnc003.mcc123.3gppnetwork.org | 全网规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | IP地址类型（IPADDRESSTYPE） | IPTypeV4 | 全网规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[**ADD PNFPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)** | IP地址（IPV4ADDRESS1） | 192.168.126.11<br>192.168.126.12 | 全网规划 | **SMF本端添加UL CL UPF**<br>。 |
| **[ADD PNFNS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md)** | 索引（INDEX） | 3 | 本端规划 | **配置用户面支持的服务切片信息**<br>。 |
| **[ADD PNFNS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | **配置用户面支持的服务切片信息**<br>。 |
| **[ADD PNFNS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md)** | 切片/服务类型（SST） | 1 | 全网规划 | **配置用户面支持的服务切片信息**<br>。 |
| **[ADD PNFNS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md)** | 切片分类器（SD） | 010101 | 全网规划 | **配置用户面支持的服务切片信息**<br>。 |
| **[**ADD PNFDNN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNN信息管理/增加对端NF的DNN信息（ADD PNFDNN）_09654342.md)** | 索引（INDEX） | 3 | 本端规划 | **配置“UL CL UPF+辅锚点UPF”的DNN属性，用于在用户会话激活时基于用户的DNN选择UL CL UPF。** |
| **[**ADD PNFDNN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNN信息管理/增加对端NF的DNN信息（ADD PNFDNN）_09654342.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | **配置“UL CL UPF+辅锚点UPF”的DNN属性，用于在用户会话激活时基于用户的DNN选择UL CL UPF。** |
| **[**ADD PNFDNN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNN信息管理/增加对端NF的DNN信息（ADD PNFDNN）_09654342.md)** | 数据网络名称（DNN） | Huawei.com | 全网规划 | **配置“UL CL UPF+辅锚点UPF”的DNN属性，用于在用户会话激活时基于用户的DNN选择UL CL UPF。** |
| [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md) | 索引（INDEX） | 1 | 本端规划 | **为“UL CL UPF+辅锚点UPF”添加DNAI信息。** |
| [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md) | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | **为“UL CL UPF+辅锚点UPF”添加DNAI信息。** |
| [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md) | 数据网络访问标识（DNAI） | testdnai | 本端规划 | **为“UL CL UPF+辅锚点UPF”添加DNAI信息。** |
| [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md) | 对端NF的DNN索引（PNFDNNINDEX） | 3 | 全网规划 | **为“UL CL UPF+辅锚点UPF”添加DNAI信息。** |
| [**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md) | UPF实例名称（NFINSTANCENAME） | UPF_Instance_0 | 全网规划 | **配置UL CL UPF的属性。**<br>“UPF共享开关”<br>用于控制UPF是否作为主、辅锚点共享UPF使用。 |
| [**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md) | UP位置特征（LOCATION） | Local | 全网规划 | **配置UL CL UPF的属性。**<br>“UPF共享开关”<br>用于控制UPF是否作为主、辅锚点共享UPF使用。 |
| [**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md) | UP支持功能（UPFUNCTION） | UlClAndBp | 全网规划 | **配置UL CL UPF的属性。**<br>“UPF共享开关”<br>用于控制UPF是否作为主、辅锚点共享UPF使用。 |
| [**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md) | UPF共享开关（SHAREDUPFSW） | ENABLE | 本端规划 | **配置UL CL UPF的属性。**<br>“UPF共享开关”<br>用于控制UPF是否作为主、辅锚点共享UPF使用。 |
| **[ADD VIRTUALUPFID](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/虚拟UPF绑定管理/增加虚拟UPF实例标识（ADD VIRTUALUPFID）_76311126.md)** | UPF实例标识（UPFINSTANCEID） | UPF_Instance_0 | 全网规划 | 配置虚拟UPF实例标识和DNAI的绑定关系。<br>UPF作为主、辅锚点和UL CL共部署体时通过将UPF划分为虚拟UPF，并和DNAI绑定来辅助用户面区分不同的辅锚点。 |
| **[ADD VIRTUALUPFID](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/虚拟UPF绑定管理/增加虚拟UPF实例标识（ADD VIRTUALUPFID）_76311126.md)** | 虚拟UPF实例标识（VUPFINSTANCEID） | v_UPF_Instance_0 | 本端规划 | 配置虚拟UPF实例标识和DNAI的绑定关系。<br>UPF作为主、辅锚点和UL CL共部署体时通过将UPF划分为虚拟UPF，并和DNAI绑定来辅助用户面区分不同的辅锚点。 |
| **[ADD VUPFIDBINDDNAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/DNAI绑定管理/增加虚拟UPF实例标识的DNAI（ADD VUPFIDBINDDNAI）_76311127.md)** | 虚拟UPF实例标识（VUPFINSTANCEID） | v_UPF_Instance_0 | 本端规划 | 配置虚拟UPF实例标识和DNAI的绑定关系。<br>UPF作为主、辅锚点和UL CL共部署体时通过将UPF划分为虚拟UPF，并和DNAI绑定来辅助用户面区分不同的辅锚点。 |
| **[ADD VUPFIDBINDDNAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/DNAI绑定管理/增加虚拟UPF实例标识的DNAI（ADD VUPFIDBINDDNAI）_76311127.md)** | 数据网络访问标识（DNAI） | testdnai | 全网规划 | 配置虚拟UPF实例标识和DNAI的绑定关系。<br>UPF作为主、辅锚点和UL CL共部署体时通过将UPF划分为虚拟UPF，并和DNAI绑定来辅助用户面区分不同的辅锚点。 |
| **[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)** | 跟踪区标识（TAI） | 1230320101 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 索引（INDEX） | 1 | 本端规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 移动国家码（MCC） | 460 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 移动网号（MNC） | 03 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 查询方式（QUERYTYPE） | START_END | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 起始号段（RANGESTART） | 12303260101 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[**ADD PNFTAIRANGE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)** | 终止号段（RANGEEND） | 12303260103 | 全网规划 | 配置园区UPF覆盖的TAI区域信息。<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>用于单个TAI的配置，<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>则可用来添加一个TAI范围。具体使用<br>**[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**<br>还是<br>**[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**<br>取决于园区范围的分布情况。 |
| **[ADD UPAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/UP区域管理/增加UPF服务区（ADD UPAREA）_09652457.md)** | UP位置区名称（AREANAME） | UPAREA1 | 全网规划 | **配置用于SMF本端判定UL CL UPF归属区域的区域类型，如TA类型。** |
| **[ADD UPAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/UP区域管理/增加UPF服务区（ADD UPAREA）_09652457.md)** | AREA类型（AREATYPE） | N2TAI | 全网规划 | **配置用于SMF本端判定UL CL UPF归属区域的区域类型，如TA类型。** |
| [**ADD UPAREABINDN2TAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/TAI绑定UP区域/增加UPF服务区名称绑定的5G TAI范围（ADD UPAREABINDN2TAI）_09653098.md) | UP位置区名称（AREANAME） | UPAREA1 | 全网规划 | **为UPAREA1添加区域范围。** |
| [**ADD UPAREABINDN2TAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/TAI绑定UP区域/增加UPF服务区名称绑定的5G TAI范围（ADD UPAREABINDN2TAI）_09653098.md) | N2TAI范围开始值（N2BEGINTAI） | 1230320101 | 全网规划 | **为UPAREA1添加区域范围。** |
| [**ADD UPAREABINDN2TAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/TAI绑定UP区域/增加UPF服务区名称绑定的5G TAI范围（ADD UPAREABINDN2TAI）_09653098.md) | N2TAI范围结束值（N2ENDTAI） | 1230320103 | 全网规划 | **为UPAREA1添加区域范围。** |
| **[ADD PNFSMFSERAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端SMF服务区管理/增加对端NF的SMF服务区域信息（ADD PNFSMFSERAREA）_09653019.md)** | NF实例标识（NFINSTANCEID） | UPF_Instance_0 | 全网规划 | **SMF本端配置UL CL UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UL CL UPF。** |
| **[ADD PNFSMFSERAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端SMF服务区管理/增加对端NF的SMF服务区域信息（ADD PNFSMFSERAREA）_09653019.md)** | SMF服务区域（SMFSERVINGAREA） | UPAREA1 | 全网规划 | **SMF本端配置UL CL UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UL CL UPF。** |

## [操作步骤](#ZH-CN_OPI_0231367702)

1. 进入 “MML命令行-UNC” 窗口。
2. **SMF本端添加UL CL UPF** 。
  **[ADD PNFPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)**
3. **配置用户面支持的服务切片信息** 。
  **[ADD PNFNS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例切片信息管理/增加对端NF的切片信息（ADD PNFNS）_09652622.md)**
4. **配置UL CL UPF的DNN属性** 。
  **[ADD PNFDNN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNN信息管理/增加对端NF的DNN信息（ADD PNFDNN）_09654342.md)**
5. **为UL CL UPF添加DNAI信息。**
  [**ADD PNFDNAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端DNAI信息管理/增加对端NF的DNAI信息（ADD PNFDNAI）_09652965.md)
6. **配置UL CL UPF的属性。**
  [**ADD UPNODE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md)
7. **（可选）配置虚拟UPF实例标识和DNAI的绑定关系。** 如果UPF为主、辅锚点共部署实体，可配置此步骤。
    - **配置虚拟UPF实例**。
      **[ADD VIRTUALUPFID](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/虚拟UPF绑定管理/增加虚拟UPF实例标识（ADD VIRTUALUPFID）_76311126.md)**
    - **配置虚拟UPF实例和DNAI的绑定关系。**
      **[ADD VUPFIDBINDDNAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/虚拟UPF管理/DNAI绑定管理/增加虚拟UPF实例标识的DNAI（ADD VUPFIDBINDDNAI）_76311127.md)**
8. **（可选）配置UPF服务区域。** 如果园区UPF规划了UPF服务区域，可通过此步骤绑定其对应的TAI。
    - **配置用于SMF本端判定UL CL UPF归属区域的区域类型**。
      **[ADD UPAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/UP区域管理/增加UPF服务区（ADD UPAREA）_09652457.md)**
    - **配置UL CL UPF归属区域对应的区域范围。**
      [**ADD UPAREABINDN2TAI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP跟踪区管理/TAI绑定UP区域/增加UPF服务区名称绑定的5G TAI范围（ADD UPAREABINDN2TAI）_09653098.md)
    - **SMF本端配置UL CL UPF所覆盖的区域**。
      **[ADD PNFSMFSERAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端SMF服务区管理/增加对端NF的SMF服务区域信息（ADD PNFSMFSERAREA）_09653019.md)**
9. **（可选）配置园区UPF覆盖的TAI区域信息。** 如果园区UPF未规划UPF服务区域，可通过此步骤添加其对应的TAI。
    - （可选）园区范围处于某单个TAI内，配置园区UPF和TAI的关系。
      **[ADD PNFTAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI信息/增加对端NF的TAI信息（ADD PNFTAI）_09652455.md)**
    - （可选）园区范围跨了若干个TAI，配置园区UPF和TAI范围的关系。
      **[ADD PNFTAIRANGE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例TAI范围管理/增加对端NF的TAI范围（ADD PNFTAIRANGE）_09652649.md)**
10. **（可选）用户在园区外通过专用DNN访问园区业务时，若不允许插入I-UPF对数据报文进行转接，可配置专用DNN下不允许插入I-UPF** 。
  **[ADD IUPFAPNDPMODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UPF选择管理/I-UPF部署策略/APN粒度的I-UPF部署模式/增加I-UPF在特定园区专用APN下的部署模式配置（ADD IUPFAPNDPMODE）_76930386.md)**
  > **说明**
  > **NGDEPLOYMODE** 参数若设置为NOIUPF，会导致终端移动到园区外时拒绝接入。

## [任务示例](#ZH-CN_OPI_0231367702)

任务描述

**示例1**

运营商要为某企业园区内的用户提供UL CL业务，对于进入园区的用户访问园区内的服务时，数据流就近在园区内DC卸载。

现网主锚点UPF和“UL CL UPF+辅锚点UPF”分离部署，且为园区UPF规划了UPF服务区域，UPF覆盖的TA区域为“1230320101”~“1230320103”。

假定该园区的APN为Huawei1.com，对应的UPF实例标志分别为UPF_Instance_0，对应的IP地址为192.168.126.11。

**示例2**

运营商要为某企业园区内的用户提供UL CL业务，对于进入园区的用户访问园区内的服务时，数据流就近在园区内DC卸载。

现网主锚点UPF和“UL CL UPF+辅锚点UPF”合一部署，园区对应的一个特定的TAI，UPF覆盖的TA区域为“1230320105”。

假定该园区的APN为Huawei2.com，对应的UPF实例标志分别为UPF_Instance_0，对应的IP地址为192.168.126.11。

脚本

**示例1**

// **SMF本端添加UPF** 。

```
ADD PNFPROFILE:NFINSTANCEID="UPF_Instance_0", NFTYPE=NfUPF, NFSTATUS=Registered,FQDN="upf00.node.mnc003.mcc123.3gppnetwork.org",IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="192.168.126.11";
```

// **配置用户面支持的服务切片信息** 。

```
ADD PNFNS: INDEX=3, NFINSTANCEID="UPF_Instance_0", SST=1, SD="000001";
```

// **配置UPF的DNN属性** 。

```
ADD PNFDNN:INDEX=3, NFINSTANCEID="UPF_Instance_0", DNN="Huawei1.com";
```

// **为UL CL UPF添加DNAI信息。**

```
ADD PNFDNAI: INDEX=1,NFINSTANCEID="UPF_Instance_0", DNAI="testdnai",PNFDNNINDEX=3;
```

// **配置UPF的属性。**

```
ADD UPNODE:NFINSTANCENAME="UPF_Instance_0", LOCATION=Local, UPFUNCTION=UlClAndBp;
```

// **配置用于SMF本端判定UPF归属区域的区域类型** 。

```
ADD UPAREA:AREANAME="UPAREA1", AREATYPE=N2TAI; 
```

// **配置UL CL UPF归属区域对应的区域范围。**

```
ADD UPAREABINDN2TAI:AREANAME="UPAREA1", N2BEGINTAI="12303260101", N2ENDTAI="12303260103";
```

// **SMF本端配置UPF所覆盖的区域** 。

```
ADD PNFSMFSERAREA:NFINSTANCEID="UPF_Instance_0", SMFSERVINGAREA="UPAREA1";
```

**示例2**

// **SMF本端添加UPF** 。

```
ADD PNFPROFILE:NFINSTANCEID="UPF_Instance_0", NFTYPE=NfUPF, NFSTATUS=Registered,FQDN="upf00.node.mnc003.mcc123.3gppnetwork.org",IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="192.168.126.11";
```

// **配置用户面支持的服务切片信息** 。

```
ADD PNFNS: INDEX=3, NFINSTANCEID="UPF_Instance_0", SST=1, SD="000001";
```

// **配置UPF的DNN属性** 。

```
ADD PNFDNN:INDEX=3, NFINSTANCEID="UPF_Instance_0", DNN="Huawei2.com";
```

// **为UL CL UPF添加DNAI信息。**

```
ADD PNFDNAI: INDEX=1,NFINSTANCEID="UPF_Instance_0", DNAI="testdnai",PNFDNNINDEX=3;
```

// **配置UPF的属性。**

```
ADD UPNODE:NFINSTANCENAME="UPF_Instance_0", LOCATION=Local, UPFUNCTION=UlClAndBp;
```

// **配置园区UPF覆盖的TAI区域信息** 。

```
ADD PNFTAI: NFINSTANCEID="UPF_Instance_0",TAI="12303260105";
```
